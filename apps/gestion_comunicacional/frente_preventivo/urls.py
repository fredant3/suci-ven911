from django.urls import path, include


urlpatterns = [
    path(
        "frente-preventivo/",
        include(
            (
                "apps.gestion_comunicacional.frente_preventivo.urls_webs",
                "frentepreventivo",
            )
        ),
    ),
    path(
        "api/frente-preventivo/",
        include(
            (
                "apps.gestion_comunicacional.frente_preventivo.urls_apis",
                "api_frentepreventivo",
            )
        ),
    ),
]
