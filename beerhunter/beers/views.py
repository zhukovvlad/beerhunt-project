from django.views.generic import ListView

from .models import Beer


class BeerListView(ListView):
    model = Beer
