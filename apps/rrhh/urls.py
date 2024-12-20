from django.urls import include, path

urlpatterns = [
    path("cargos/", include(("apps.rrhh.cargos.urls", "cargos"))),
    path(
        "api/cargos/",
        include(("apps.rrhh.cargos.urls_apis", "api_cargos")),
    ),
]
