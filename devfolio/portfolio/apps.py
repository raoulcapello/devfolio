from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PortfolioConfig(AppConfig):
    name = "devfolio.portfolio"
    verbose_name = _("Portfolio")
