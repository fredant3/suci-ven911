from django.urls import include, path
from potencia.views import PotenciaView

urlpatterns = [
    path("", PotenciaView.as_view(), name="potencia"),
    path("incidencias/", include(("apps.potencia.incidencias.urls", "incidencias"))),
    path(
        "api/incidencias/",
        include(("apps.potencia.incidencias.urls_apis", "api_incidencias")),
    ),
    path(
        "tipoIncidencia/",
        include(("apps.potencia.tipoIncidencia.urls", "tipoIncidencia")),
    ),
    path(
        "api/tipoIncidencia/",
        include(("apps.potencia.tipoIncidencia.urls_apis", "api_tipoIncidencia")),
    ),
    path(
        "unidad-respuesta-inmediata/",
        include(("apps.potencia.uri.urls", "uri")),
    ),
    path(
        "api/unidad-respuesta-inmediata/",
        include(("apps.potencia.uri.urls_apis", "api_uri")),
    ),
]
