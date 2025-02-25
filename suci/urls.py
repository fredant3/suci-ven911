from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", include(("apps.users.auth.urls", "auth"))),
    path("api/auth/", include(("apps.users.auth.urls_apis", "api_auth"))),
    path("dashboard/", include(("apps.dashboard.modules.urls", "modules"))),
    path("gestion-administrativa/", include(("apps.administracion.urls"))),
    path("asesoria-juridica/", include(("apps.asesoria.urls"))),
    path("biblioteca/", include(("apps.biblioteca.urls"))),
    path("organizacion/", include(("apps.organizacion.urls"))),
    path("emergencia/", include(("apps.emergencia.urls"))),
    path("emergencia/", include("apps.emergencia.urls")),
    path("planificacion/", include(("apps.planificacion.urls"))),
    path("presupuesto/", include(("apps.presupuesto.urls"))),
    path("potencia/", include(("apps.potencia.urls"))),
    path("gestion-humana/", include(("apps.rrhh.urls"))),
    path("seguridad/", include(("apps.seguridad.urls"))),
    path("tecnologia/", include(("apps.tecnologia.urls"))),
    path("", RedirectView.as_view(url="dashboard", permanent=True)),
]
