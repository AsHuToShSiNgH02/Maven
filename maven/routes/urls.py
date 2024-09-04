# routes/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SafetyPointViewSet

router = DefaultRouter()
router.register(r'safety-points', SafetyPointViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
