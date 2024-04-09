# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from sismic_api.sismic_data.views import sismic_data as sismic_data_views

router = DefaultRouter()
router.register(r'sismic_data', sismic_data_views.FeatureListViewSet, basename='sismic_data')

urlpatterns = [
    path('', include(router.urls))
]