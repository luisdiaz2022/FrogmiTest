"""Admon Model."""

# Django
from django.contrib import admin

# Models
from sismic_api.sismic_data.models import Feature


class CustomUserAdmin(admin.ModelAdmin):
    """user model admin."""

    list_display = ('external_id', 'magnitude', 'place', 'time', 'tsunami', 'mag_type', 'title', 'longitude', 'latitude')
    list_filter = ('mag_type', 'tsunami')


admin.site.register(Feature, CustomUserAdmin)