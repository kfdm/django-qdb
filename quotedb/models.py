from django.db import models
from django.utils.translation import ugettext_lazy as _


class Quote(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    body = models.TextField(verbose_name=_('body'))
    owner = models.ForeignKey('auth.User', verbose_name=_('owner'), on_delete=models.CASCADE)
    approved = models.BooleanField(default=False, verbose_name=_('approved'))

    class Meta:
        verbose_name = _('quote')
        verbose_name_plural = _('quotes')
        ordering = ('-created',)
