from reporte.views import ReporteView
from django.urls import include, path

urlpatterns = [
    path("", ReporteView.as_view(), name="index"),
    path(
        "reportes_administracion/",
        include(
            ("apps.reporte.reportes_administracion.urls", "reportes_administracion")
        ),
    ),
    path(
        "api/reportes_administracion/",
        include(
            (
                "apps.reporte.reportes_administracion.urls_apis",
                "api_reportes_administracion",
            )
        ),
    ),
    # path(
    #    "averias/",
    #    include(("apps.administracion.averia.urls", "averias")),
    # ),
    # path(
    #    "api/averias/",
    #    include(("apps.administracion.averia.urls_apis", "api_averias")),
    # ),
    # path(
    #    "compras/",
    #    include(("apps.administracion.compras.urls", "compras")),
    # ),
    # path(
    #    "api/compras/",
    #    include(("apps.administracion.compras.urls_apis", "api_compras")),
    # ),
    # path(
    #    "departamentos/",
    #    include(("apps.administracion.departamentos.urls", "departamentos")),
    # ),
    # path(
    #    "api/departamentos/",
    #    include(("apps.administracion.departamentos.urls_apis", "api_departamentos")),
    # ),
    # path(
    #    "articulos/",
    #    include(("apps.administracion.inventario.urls", "articulos")),
    # ),
    # path(
    #    "api/articulos/",
    #    include(("apps.administracion.inventario.urls_apis", "api_articulos")),
    # ),
    # path(
    #    "sedes/",
    #    include(("apps.administracion.sedes.urls", "sedes")),
    # ),
    # path(
    #    "api/sedes/",
    #    include(("apps.administracion.sedes.urls_apis", "api_sedes")),
    # ),
    # path(
    #    "tipo_averia/",
    #    include(("apps.administracion.tipo_averia.urls", "tipo_averias")),
    # ),
    # path(
    #    "api/tipo_averia/",
    #    include(("apps.administracion.tipo_averia.urls_apis", "api_tipo_averias")),
    # ),
]
