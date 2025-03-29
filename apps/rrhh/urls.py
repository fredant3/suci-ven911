from django.urls import include, path
from apps.rrhh.views import GestionHumanaView

urlpatterns = [
    path("", GestionHumanaView.as_view(), name="gestion_humana"),
    path("empleados/", include(("apps.rrhh.empleados.urls", "empleados"))),
    path(
        "api/empleados/",
        include(("apps.rrhh.empleados.urls_apis", "api_empleados")),
    ),
    path(
        "tipos-empleados/",
        include(("apps.rrhh.tipos_empleados.urls", "tipos_empleados")),
    ),
    path(
        "api/tipos-empleados/",
        include(("apps.rrhh.tipos_empleados.urls_apis", "api_tipos_empleados")),
    ),
    path("cargos/", include(("apps.rrhh.cargos.urls", "cargos"))),
    path(
        "api/cargos/",
        include(("apps.rrhh.cargos.urls_apis", "api_cargos")),
    ),
    path("cuentas/", include(("apps.rrhh.cuentas.urls", "cuentas"))),
    path(
        "api/cuentas/",
        include(("apps.rrhh.cuentas.urls_apis", "api_cuentas")),
    ),
    path("dotaciones/", include(("apps.rrhh.dotaciones.urls", "dotaciones"))),
    path(
        "api/dotaciones/",
        include(("apps.rrhh.dotaciones.urls_apis", "api_dotaciones")),
    ),
    path("educaciones/", include(("apps.rrhh.educaciones.urls", "educaciones"))),
    path(
        "api/educaciones/",
        include(("apps.rrhh.educaciones.urls_apis", "api_educaciones")),
    ),
    path("familiares/", include(("apps.rrhh.familiares.urls", "familiares"))),
    path(
        "api/familiares/",
        include(("apps.rrhh.familiares.urls_apis", "api_familiares")),
    ),
    path("sueldos/tipos", include(("apps.rrhh.tipos_sueldos.urls", "tipos_sueldos"))),
    path(
        "api/sueldos/tipos/",
        include(("apps.rrhh.tipos_sueldos.urls_apis", "api_tipos_sueldos")),
    ),
    path("contratos/", include(("apps.rrhh.contratos.urls", "contratos"))),
    path(
        "api/contratos/",
        include(("apps.rrhh.contratos.urls_apis", "api_contratos")),
    ),
]
