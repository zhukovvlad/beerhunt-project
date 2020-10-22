from django.shortcuts import render
from django.views.generic import TemplateView

from beerhunter.beers.models import Beer


class HomePageView(TemplateView):
    template_name = "home.html"
