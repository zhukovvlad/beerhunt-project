from django.urls import path

from . import views


app_name = "breweries"
urlpatterns = [
    path(
        route='',
        view=views.BreweryListView.as_view(),
        name='BreweryList'
    ),
    path(
        route='add/',
        view=views.BreweryCreateView.as_view(),
        name='add'
    ),
    path(
        route='<slug:slug>/',
        view=views.BreweryDetailView.as_view(),
        name='BreweryDetail'
    ),
]
