from django.urls import path

from rrhh.tipos_empleados.views.create_view import TipoEmpleadoCreateView
from rrhh.tipos_empleados.views.delete_view import TipoEmpleadoDeleteView
from rrhh.tipos_empleados.views.list_view import TipoEmpleadoListView
from rrhh.tipos_empleados.views.update_view import TipoEmpleadoUpdateView
from rrhh.tipos_empleados.views.export_view import TipoEmpleadoExcelView

urlpatterns = [
    path(
        "",
        TipoEmpleadoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        TipoEmpleadoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        TipoEmpleadoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        TipoEmpleadoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TipoEmpleadoDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export/excel",
        TipoEmpleadoExcelView.as_view(),
        name="export_excel",
    ),
]
