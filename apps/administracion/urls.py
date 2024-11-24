from django.urls import include, path

urlpatterns = [
    path(
        "administracion/",
        include(("apps.administracion.asgnaciones.urls", "asgnaciones")),
    ),
    path(
        "api/administracion/",
        include(("apps.administracion.asgnaciones.urls_apis", "api_asgnaciones")),
    ),
]
