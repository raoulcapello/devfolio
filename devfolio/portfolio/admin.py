from django.contrib import admin

from .models import Portfolio, Project, Screenshot, Tag, VideoURL

admin.site.register(Portfolio)
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Screenshot)
admin.site.register(VideoURL)
