from django.urls import path, include

from gestion_comunicacional.info.InfoController import InfoController

urlpatterns = [
    path("", InfoController.as_view(), name="gc_info"),
    path(
        "gestion-comunicacional/",
        include(("apps.gestion_comunicacional.urls_webs", "gestioncomunicacional")),
    ),
    path(
        "api/gestion-comunicacional/",
        include(("apps.gestion_comunicacional.urls_apis", "api_gestioncomunicacional")),
    ),
    path("", InfoController.as_view(), name="gc_info"),
    path(
        "gestion-comunicacional/",
        include(("apps.gestion_comunicacional.urls_webs", "GestionComunicacional")),
    ),
    path(
        "api/gestion-comunicacional/",
        include(("apps.gestion_comunicacional.urls_apis", "api_GestionComunicacional")),
    ),
]
