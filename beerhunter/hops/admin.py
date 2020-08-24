from django.contrib import admin

from .models import Hop, AromaProfile


@admin.register(Hop)
class HopAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'country_of_origin',
        'alpha_min',
        'alpha_max',
    )


admin.site.register(AromaProfile)
