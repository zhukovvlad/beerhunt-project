from django.urls import path

from . import views


app_name = "beers"
urlpatterns = [
    path(
        route='',
        view=views.BeerListView.as_view(),
        name='BeerList'
    ),
    path(
        route='add/',
        view=views.BeerCreateView.as_view(),
        name='add'
    ),
    path(
        route='<slug:slug>/',
        view=views.BeerDetailView.as_view(),
        name='BeerDetail'
    )
]
