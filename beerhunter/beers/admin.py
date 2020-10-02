from django.contrib import admin

from .models import Beer, Style


@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


admin.site.register(Style)
