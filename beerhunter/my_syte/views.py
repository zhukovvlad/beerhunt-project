# from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Max, Count

from beerhunter.beers.models import Beer
from beerhunter.hops.models import Hop

# from beerhunter.beers.models import Beer


class HomePageView(TemplateView):
    template_name = "my_syte/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        qs = Beer.objects.all_with_related_instances_and_score()

        top_rating = qs.aggregate(Max('score'))
        top_beer = qs.filter(score=top_rating['score__max'])

        top_ibu = qs.aggregate(Max('ibu'))
        top_ibu_beer = qs.filter(ibu=top_ibu['ibu__max'])

        qs_hop = Hop.objects.all_with_prefetch_beers().annotate(count_beers=Count('brewed_beers'))
        qs_hop_max = qs_hop.aggregate(Max('count_beers'))
        top_hop = qs_hop.filter(count_beers=qs_hop_max['count_beers__max'])

        context["max_score"] = top_rating['score__max']
        context["top_beer"] = top_beer
        context["top_ibu"] = top_ibu['ibu__max']
        context["top_ibu_beer"] = top_ibu_beer
        context["qs_hop_max"] = qs_hop_max['count_beers__max']
        context["top_hop"] = top_hop
        return context
