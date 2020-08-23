from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Beer


class BeerListView(ListView):
    model = Beer


class BeerDetailView(DetailView):
    model = Beer


class BeerCreateView(LoginRequiredMixin, CreateView):
    model = Beer
    template_name = "beers/beer_form.html"

    fields = [
        'title',
        'description',
        'brewery',
        'og',
        'abv',
        'ibu'
    ]
