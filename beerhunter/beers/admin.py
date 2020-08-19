from django.contrib import admin

from .models import Beer


@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
