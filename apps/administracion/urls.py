from django.urls import include, path

urlpatterns = [
    path(
        "asgnaciones/",
        include(("apps.administracion.asignaciones.urls", "asgnaciones")),
    ),
    path(
        "api/asgnaciones/",
        include(("apps.administracion.asignaciones.urls_apis", "api_asgnaciones")),
    ),
    path(
        "averias/",
        include(("apps.administracion.averia.urls", "averias")),
    ),
    path(
        "api/averias/",
        include(("apps.administracion.averia.urls_apis", "api_averias")),
    ),
    path(
        "articulos/",
        include(("apps.administracion.inventario.urls", "articulos")),
    ),
    path(
        "api/articulos/",
        include(("apps.administracion.inventario.urls_apis", "api_articulos")),
    ),
]
