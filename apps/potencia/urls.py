from django.urls import include, path

urlpatterns = [
    path("incidencias/", include(("apps.potencia.incidencias.urls", "incidencias"))),
    path(
        "api/incidencias/",
        include(("apps.potencia.incidencias.urls_apis", "api_incidencias")),
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
