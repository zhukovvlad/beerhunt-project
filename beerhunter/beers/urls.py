from django.urls import path

from . import views


app_name = "beer"
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
    ),
    path(
        route='<int:beer_id>/vote',
        view=views.CreateVote.as_view(),
        name='CreateVote'
    ),
    path(
        route='<int:beer_id>/vote/<int:pk>',
        view=views.UpdateVote.as_view(),
        name='UpdateVote'
    ),
]
