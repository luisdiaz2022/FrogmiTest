"""Admon Model."""

# Django
from django.contrib import admin

# Models
from sismic_api.sismic_data.models import Feature, Comment


class FeatureAdmin(admin.ModelAdmin):
    """user model admin."""

    list_display = ('external_id', 'magnitude', 'place', 'time', 'tsunami', 'mag_type', 'title', 'longitude', 'latitude')
    list_filter = ('mag_type', 'tsunami')

class CommentAdmin(admin.ModelAdmin):
    """Admin view for Comment model."""
    list_display = ('feature_external_id', 'body', 'created_at')  

    def feature_external_id(self, obj):
        return obj.feature.external_id

    feature_external_id.short_description = 'Feature External ID'

admin.site.register(Feature, FeatureAdmin)
admin.site.register(Comment, CommentAdmin)