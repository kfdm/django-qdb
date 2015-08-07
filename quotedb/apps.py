from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class QuoteDBConfig(AppConfig):
    name = 'quotedb'
    verbose_name = _("Quote Database")
