from rest_framework import filters, permissions, routers, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from quotedb.models import Quote
from quotedb.permissions import IsOwnerOrReadOnly
from quotedb.serializers import QuoteSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend,)
    search_fields = ('body',)
    filter_fields = ('approved',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @list_route()
    def random(self, request):
        queryset = Quote.objects.order_by('?').first()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'^', QuoteViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls
