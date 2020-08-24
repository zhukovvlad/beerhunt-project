from django.views.generic import ListView, DetailView

from .models import Hop


class HopListView(ListView):
    model = Hop
    template_name = "hops/hop_list.html"


class HopDetailView(DetailView):
    model = Hop
    template_name = "hops/hop_detail.html"
