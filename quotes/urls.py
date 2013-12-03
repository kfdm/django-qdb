from django.conf.urls import patterns, url
from django.views.generic.list import ListView
from quotes.models import Quote

urlpatterns = patterns('',
    url('^$',
        name='quotes_index',
        view=ListView.as_view(
            queryset=Quote.objects.all(),
            template_name='quote_list_page.html'
            ),
        ),
    url('^recent/',
        name='quotes_recent',
        view=ListView.as_view(
            queryset=Quote.objects.order_by('created_on'),
            template_name='quote_list_page.html'
            ),
        ),
    url('^(?P<object_id>\d+)/$',
        name='quotes_view',
        view=ListView.as_view(
            queryset=Quote.objects.all(),
            template_name='quote_detail.html'
            ),
        ),
)
