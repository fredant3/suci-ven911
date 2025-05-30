from apps.reporte.reportes_administracion.views.create_view import (
    ReportesAdministracionCreateApiView,
)
from apps.reporte.reportes_administracion.views.delete_view import (
    ReportesAdministracionDeleteApiView,
)
from apps.reporte.reportes_administracion.views.list_view import (
    ReportesAdministracionListApiView,
)
from apps.reporte.reportes_administracion.views.update_view import (
    ReportesAdministracionUpdateApiView,
)

from django.urls import path

urlpatterns = [
    path(
        "",
        ReportesAdministracionListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        ReportesAdministracionCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        ReportesAdministracionUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ReportesAdministracionDeleteApiView.as_view(),
        name="delete",
    ),
]
