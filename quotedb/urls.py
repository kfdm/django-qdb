from django.conf.urls import url

from quotedb import views

app_name = 'quotes'
urlpatterns = [
    url(r'^$', views.QuoteList.as_view(), name='quote-list'),
]
