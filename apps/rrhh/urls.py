from django.urls import include, path

urlpatterns = [
    path("cargos/", include(("apps.rrhh.cargos.urls", "cargos"))),
    path(
        "api/cargos/",
        include(("apps.rrhh.cargos.urls_apis", "api_cargos")),
    ),
    path("sueldos/tipos", include(("apps.rrhh.tipos_sueldos.urls", "tipos_sueldos"))),
    path(
        "api/sueldos/tipos/",
        include(("apps.rrhh.tipos_sueldos.urls_apis", "api_tipos_sueldos")),
    ),
]
