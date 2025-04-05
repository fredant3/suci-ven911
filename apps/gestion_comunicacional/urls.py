from django.urls import path, include

from gestion_comunicacional.info import InfoController

urlpatterns = [
    path("", InfoController.as_view(), name="gc_info"),
]
