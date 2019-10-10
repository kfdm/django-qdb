from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from quotedb import rest

router = routers.DefaultRouter()
router.register("quotes", rest.QuoteViewSet)

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("api/", include((router.urls, "api"), namespace="api")),
    path("", include(("quotedb.urls", "quotes"), namespace="quotes")),
]

try:
    import debug_toolbar
except ImportError:
    pass
else:
    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
