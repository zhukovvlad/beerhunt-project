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
        route='<slug:slug>/',
        view=views.BeerDetailView.as_view(),
        name='BeerDetail'
    )
]
