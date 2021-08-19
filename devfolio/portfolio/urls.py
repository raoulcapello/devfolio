from django.urls import path

from . import views

app_name = "portfolio"
urlpatterns = [
    path("", views.portfolio_home, name="home"),
    path("list/", views.portfolio_list, name="list"),
    path("<int:id>/", views.portfolio_detail, name="detail"),
]
