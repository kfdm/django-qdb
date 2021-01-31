from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Quote(models.Model):
    created = models.DateTimeField(verbose_name=_("created"), default=timezone.now)
    body = models.TextField(verbose_name=_('body'))
    owner = models.ForeignKey('auth.User', verbose_name=_('owner'), on_delete=models.CASCADE)
    approved = models.BooleanField(default=False, verbose_name=_('approved'))

    class Meta:
        verbose_name = _('quote')
        verbose_name_plural = _('quotes')
        ordering = ('-created',)
