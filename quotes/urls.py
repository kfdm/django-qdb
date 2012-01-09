from django.conf.urls.defaults import patterns, url
from django.views.generic import list_detail
from quotes.models import Quote

urlpatterns = patterns('',
    url('^/$',
        name='quotes_index',
        view=list_detail.object_list,
        kwargs={
            'queryset': Quote.objects.all(),
            'template_name': 'quote_list_page.html',
            },
        ),
    url('^/recent/',
        name='quotes_recent',
        view=list_detail.object_list,
        kwargs={
            'queryset': Quote.objects.order_by('created_on'),
            'template_name': 'quote_list_page.html',
            },
        )
)
