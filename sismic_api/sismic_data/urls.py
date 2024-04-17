"""Sismic_data urls."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from sismic_api.sismic_data.views import features as features_views
from sismic_api.sismic_data.views import comments as comments_views

router = DefaultRouter()
router.register(r'sismic_data', features_views.FeatureListViewSet, basename='features')
router.register(
    r'sismic_data/<int:feature_id>/comments',
    comments_views.CreateCommentView,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls))
]