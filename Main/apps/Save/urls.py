# Project
from .views import SaveViewSet

# Libs
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'save', SaveViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
