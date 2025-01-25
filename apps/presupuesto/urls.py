from django.urls import include, path
from presupuesto.views import PresupuestoView

urlpatterns = [
    path("", PresupuestoView.as_view(), name="presupuesto"),
    path("acciones/", include(("apps.presupuesto.acciones.urls", "acciones"))),
    path(
        "api/acciones/",
        include(("apps.presupuesto.acciones.urls_apis", "api_acciones")),
    ),
    path(
        "asignaciones/",
        include(
            ("apps.presupuesto.asignacion.urls", "asignaciones")
        ),  # TODO: Revisar el modulo asignaciones (presupuesto | administracion)
    ),
    path(
        "api/asignaciones/",
        include(
            ("apps.presupuesto.asignacion.urls_apis", "api_asignaciones")
        ),  # TODO: Revisar el modulo asignaciones (presupuesto | administracion)
    ),
    path("cedentes/", include(("apps.presupuesto.cedente.urls", "cedentes"))),
    path(
        "api/cedentes/",
        include(("apps.presupuesto.cedente.urls_apis", "api_cedentes")),
    ),
    path("proyectos/", include(("apps.presupuesto.proyecto.urls", "proyectos"))),
    path(
        "api/proyectos/",
        include(("apps.presupuesto.proyecto.urls_apis", "api_proyectos")),
    ),
    path("receptores/", include(("apps.presupuesto.receptor.urls", "receptores"))),
    path(
        "api/receptores/",
        include(("apps.presupuesto.receptor.urls_apis", "api_receptores")),
    ),
]
