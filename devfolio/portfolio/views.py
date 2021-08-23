import re

from django.shortcuts import get_object_or_404, render

from .models import Portfolio, Project, Tag

# Hard-code the main portfolio (for now)
portfolio = Portfolio.objects.first()


def portfolio_home(request):
    items = Project.objects.all()
    tags = Tag.objects.all()
    tag_titles = [tag.title.lower() for tag in tags]
    return render(
        request,
        "pages/home.html",
        {
            "portfolio": portfolio,
            "items": items,
            "tags": tags,
            "tag_titles": tag_titles,
        },
    )


def portfolio_list(request):
    return render(request, "portfolio/list.html", {"navbar_dark": True})


def portfolio_detail(request, id):
    project = get_object_or_404(Project, id=id)
    related = Project.objects.exclude(id=id)

    # Prepare URL's for display
    live_url_short = ""
    repo_url_short = ""
    if project.live_url:
        regex_pattern = r"https?://([\w\d\.-]+)"  # Match only sld.domain.tld
        result = re.search(regex_pattern, project.live_url)
        if result:
            live_url_short = result.group(1)
    if project.repo_url:
        regex_pattern = r"https?://([\w\d\.-]+)/(.+)"  # Match only repo name
        result = re.search(regex_pattern, project.repo_url)
        if result:
            repo_url_short = result.group(2)

    return render(
        request,
        "portfolio/detail.html",
        {
            "portfolio": portfolio,
            "navbar_floating": True,
            "project": project,
            "related": related,
            "live_url_short": live_url_short,
            "repo_url_short": repo_url_short,
        },
    )
