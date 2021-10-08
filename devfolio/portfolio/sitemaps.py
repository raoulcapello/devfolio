from django.contrib.sitemaps import Sitemap

from .models import Portfolio, Project


class PortfolioSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Portfolio.objects.first()

    def lastmod(self, obj):
        return obj.date


class ProjectSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.date
