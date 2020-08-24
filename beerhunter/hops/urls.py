from django.urls import path

from . import views


app_name = "hops"
urlpatterns = [
    path(
        route='',
        view=views.HopListView.as_view(),
        name='HopList'
    ),
    path(
        route='<slug:slug>/',
        view=views.HopDetailView.as_view(),
        name='HopDetail'
    )
]
