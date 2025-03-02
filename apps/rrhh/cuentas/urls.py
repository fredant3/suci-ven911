from django.urls import path

from rrhh.cuentas.views.create_view import CuentaCreateView
from rrhh.cuentas.views.delete_view import CuentaDeleteView
from rrhh.cuentas.views.list_view import CuentaListView
from rrhh.cuentas.views.update_view import CuentaUpdateView
from rrhh.cuentas.views.export_view import CuentaExcelView

urlpatterns = [
    path(
        "",
        CuentaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        CuentaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        CuentaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        CuentaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        CuentaDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export/excel",
        CuentaExcelView.as_view(),
        name="export_excel",
    ),
]
