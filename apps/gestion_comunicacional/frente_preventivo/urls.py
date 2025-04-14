from django.urls import path, include

from gestion_comunicacional.frente_preventivo.info.InfoController import InfoController

urlpatterns = [
    path("", InfoController.as_view(), name="gc_info"),
    path(
        "frente-preventivo/",
        include(
            (
                "apps.gestion_comunicacional.frentepreventivo.urls_webs",
                "frentepreventivo",
            )
        ),
    ),
    path(
        "api/frente-preventivo/",
        include(
            (
                "apps.gestion_comunicacional.frentepreventivo.urls_apis",
                "api_frentepreventivo",
            )
        ),
    ),
    path("", InfoController.as_view(), name="gc_info"),
    path(
        "frente-preventivo/",
        include(
            (
                "apps.gestion_comunicacional.frentepreventivo.urls_webs",
                "FrentePreventivo",
            )
        ),
    ),
    path(
        "api/frente-preventivo/",
        include(
            (
                "apps.gestion_comunicacional.frentepreventivo.urls_apis",
                "api_FrentePreventivo",
            )
        ),
    ),
]
