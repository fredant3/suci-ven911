from django.urls import path

from rrhh.tipos_empleados.views.create_view import TipoEmpleadoCreateApiView
from rrhh.tipos_empleados.views.delete_view import TipoEmpleadoDeleteApiView
from rrhh.tipos_empleados.views.list_view import TipoEmpleadoListApiView
from rrhh.tipos_empleados.views.update_view import TipoEmpleadoUpdateApiView
from rrhh.tipos_empleados.views.export_view import TipoEmpleadoExcelView

urlpatterns = [
    path(
        "",
        TipoEmpleadoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        TipoEmpleadoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        TipoEmpleadoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TipoEmpleadoDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export/excel",
        TipoEmpleadoExcelView.as_view(),
        name="export_excel",
    ),
]
