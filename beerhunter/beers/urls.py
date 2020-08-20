from django.urls import path

from . import views


app_name = "beers"
urlpatterns = [
    path(
        route='',
        view=views.BeerListView.as_view(),
        name='BeerList'
    )
]
