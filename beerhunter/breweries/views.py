from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Brewery
from beerhunter.beers.models import Beer


class BreweryListView(ListView):
    model = Brewery


class BreweryDetailView(DetailView):
    model = Brewery

    def get_context_data(self, **kwargs):
        print(self)
        ctx = super().get_context_data(**kwargs)
        print('initial Brewery ctx is, ', ctx)
        qs_beers = Beer.objects.all_with_related_instances_and_score()
        print('qs_beers are, ', qs_beers)
        brewery_beers = qs_beers.filter(brewery=ctx['brewery'])
        brewery_rating = 0
        for item in brewery_beers:
            if not item.score:
                item.score = 0
            brewery_rating += item.score
        # brewery_rating = brewery_rating / len(brewery_beers)

        ctx['connected_beers'] = brewery_beers
        ctx['rating'] = brewery_rating
        print('Final Brewery ctx is, ', ctx)
        return ctx


class BreweryCreateView(LoginRequiredMixin, CreateView):
    model = Brewery
    template_name = "breweries/brewery_form.html"

    fields = [
        'title',
        'country_of_origin'
    ]
