from apps.reporte.reportes_administracion.views.create_view import (
    ReportesAdministracionCreateView,
)
from apps.reporte.reportes_administracion.views.delete_view import (
    ReportesAdministracionDeleteView,
)
from apps.reporte.reportes_administracion.views.list_view import (
    ReportesAdministracionListView,
)
from apps.reporte.reportes_administracion.views.update_view import (
    ReportesAdministracionUpdateView,
)


from django.urls import path

urlpatterns = [
    path(
        "",
        ReportesAdministracionListView.as_view(),
        name="list",
    ),
    path(
        "create",
        ReportesAdministracionCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        ReportesAdministracionListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        ReportesAdministracionUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ReportesAdministracionDeleteView.as_view(),
        name="delete",
    ),
]
