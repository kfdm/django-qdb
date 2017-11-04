from django.conf.urls import url

from quotedb import views

urlpatterns = [
    url(r'^$', views.QuoteList.as_view(), name='quote-list'),
]
