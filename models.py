from django.db import models
from django.contrib.auth.models import User


class Quote(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='quotes')

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        # For Django Admin Snippet
        return self.body[0:20]
