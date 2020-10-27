from django.views.generic import ListView, DetailView

from .models import Hop


class HopListView(ListView):
    # model = Hop
    queryset = Hop.objects.all_with_related_instances_and_score()
    template_name = "hops/hop_list.html"

    ordering = ['-score']


class HopDetailView(DetailView):
    model = Hop
    template_name = "hops/hop_detail.html"
