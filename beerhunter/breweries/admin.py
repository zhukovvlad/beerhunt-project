from django.contrib import admin

from .models import Brewery


@admin.register(Brewery)
class BreweryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
