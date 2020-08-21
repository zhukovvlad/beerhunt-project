from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Brewery


class BreweryListView(ListView):
    model = Brewery


class BreweryDetailView(DetailView):
    model = Brewery


class BreweryCreateView(LoginRequiredMixin, CreateView):
    model = Brewery
    template_name = "breweries/brewery_form.html"

    fields = [
        'title',
        'country_of_origin'
    ]
