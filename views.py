from rest_framework import viewsets, permissions

from rest_framework_word_filter import FullWordSearchFilter

from quotedb.models import Quote
from quotedb.permissions import IsOwnerOrReadOnly
from quotedb.serializers import QuoteSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    filter_backends = (FullWordSearchFilter,)
    word_fields = ('body',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
