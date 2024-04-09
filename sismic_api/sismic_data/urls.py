from django.urls import path
from .views import FeatureList

urlpatterns = [
    path('features/', FeatureList.as_view(), name='feature-list'),
]