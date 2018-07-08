from rest_framework import routers

import quotedb.rest as rest

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

router = routers.DefaultRouter(trailing_slash=False)
router.register('quotes', rest.QuoteViewSet)

urlpatterns = [
    url('', include(('quotedb.urls', 'quotes'))),
    url('', include(('social_django.urls', 'social'))),
    url('', include('django.contrib.auth.urls')),
    url(r'^api/', include((router.urls, 'api'))),
    url(r'^admin/', admin.site.urls),
]
