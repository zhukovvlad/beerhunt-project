from django.views.generic import ListView, DetailView

from .models import Beer


class BeerListView(ListView):
    model = Beer


class BeerDetailView(DetailView):
    model = Beer
