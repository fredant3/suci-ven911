from django.urls import path

from rrhh.cuentas.views.create_view import CuentaCreateApiView
from rrhh.cuentas.views.delete_view import CuentaDeleteApiView
from rrhh.cuentas.views.list_view import CuentaListApiView
from rrhh.cuentas.views.update_view import CuentaUpdateApiView

urlpatterns = [
    path(
        "",
        CuentaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        CuentaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        CuentaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        CuentaDeleteApiView.as_view(),
        name="delete",
    ),
]
