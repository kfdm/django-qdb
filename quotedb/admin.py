from django.contrib import admin
from quotedb.models import Quote


class QuoteAdmin(admin.ModelAdmin):
    actions = ['mark_approved', 'mark_unapproved']
    list_display = ('body', 'owner', 'approved', 'created')
    list_filter = ('approved', 'owner',)

    def mark_approved(self, request, queryset):
        rows_updated = queryset.update(approved=True)
        self.message_user(request, "%s successfully marked as approved." % rows_updated)

    def mark_unapproved(self, request, queryset):
        rows_updated = queryset.update(approved=False)
        self.message_user(request, "%s successfully marked as approved." % rows_updated)

admin.site.register(Quote, QuoteAdmin)
