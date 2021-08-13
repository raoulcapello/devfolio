from django.shortcuts import render


def portfolio_list(request):
    return render(request, "portfolio/list.html", {"navbar_dark": True})


def portfolio_detail(request, id):
    return render(request, "portfolio/detail.html", {"navbar_floating": True})
