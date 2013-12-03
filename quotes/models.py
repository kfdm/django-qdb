from django.db import models
from django.contrib.auth.models import User


class Quote(models.Model):
    body = models.TextField()
    poster = models.ForeignKey(User)
    created_on = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.body[0:20]
