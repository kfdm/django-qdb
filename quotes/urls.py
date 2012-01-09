from django.conf.urls.defaults import patterns
from django.views.generic import list_detail
from quotes.models import Quote

urlpatterns = patterns('',
    ('^/$', list_detail.object_list, {
        'queryset': Quote.objects.all(),
        'template_name': 'quote_list_page.html',
        }),
    ('^/recent/', list_detail.object_list, {
        'queryset': Quote.objects.order_by('created_on'),
        'template_name': 'quote_list_page.html',
        })
)
