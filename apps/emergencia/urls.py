from django.urls import include, path
from emergencia.views import EmergenciaView

urlpatterns = [
  
    path(
        "",
        EmergenciaView.as_view(),
        name="operaciones"
    ),
    path("operaciones", include(("apps.emergencia.operaciones.urls_webs", "operaciones"))),
    path("api/operaciones", include(("apps.emergencia.operaciones.urls_apis", "api_operaciones"))),
]
