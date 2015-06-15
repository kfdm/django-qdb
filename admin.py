from django.contrib import admin
from quotedb.models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('body', 'owner', 'approved', 'created')
    list_filter = ('approved', 'owner',)

admin.site.register(Quote, QuoteAdmin)
