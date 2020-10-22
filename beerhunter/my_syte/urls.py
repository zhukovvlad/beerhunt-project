from django.urls import path

from . import views


app_name = "site"
urlpatterns = [
    path(
        route='',
        view=views.HomePageView.as_view(),
        name='Home'
    )
]
