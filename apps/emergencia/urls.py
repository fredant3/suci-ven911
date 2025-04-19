from django.urls import include, path
from emergencia.views import EmergenciaView

urlpatterns = [
    path("", EmergenciaView.as_view(), name="operaciones"),
    
    # Rutas para operaciones
    path("operaciones/", include(("apps.emergencia.operaciones.urls_webs", "operaciones"))),
    path("api/operaciones/", include(("apps.emergencia.operaciones.urls_apis", "api_operaciones"))),
    
    # Rutas para incidencias
    path("incidencias/", include(("apps.emergencia.incidencias.urls_webs", "incidencias"))),
    path("api/incidencias/", include(("apps.emergencia.incidencias.urls_apis", "api_incidencias"))),
]