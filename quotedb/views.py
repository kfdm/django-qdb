from django.views.generic import DetailView, ListView

from quotedb import models


class QuoteDetail(DetailView):
    model = models.Quote


class QuoteList(ListView):
    queryset = models.Quote.objects.filter(approved=True)
    paginate_by = 10
