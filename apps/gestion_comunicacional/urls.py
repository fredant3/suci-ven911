from django.urls import path

from gestion_comunicacional.info.InfoController import InfoController

urlpatterns = [
    path("", InfoController.as_view(), name="gc_info"),
]
