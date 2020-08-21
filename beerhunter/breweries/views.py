from django.views.generic import ListView, DetailView

from .models import Brewery


class BreweryListView(ListView):
    model = Brewery


class BreweryDetailView(DetailView):
    model = Brewery
