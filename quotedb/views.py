from django.views.generic import DetailView, ListView

from quotedb import models


class QuoteDetail(DetailView):
    model = models.Quote


class QuoteList(ListView):
    model = models.Quote
    paginate_by = 10
