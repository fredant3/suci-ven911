from django.urls import path

from rrhh.cargos.views.create_view import CargoCreateApiView
from rrhh.cargos.views.delete_view import CargoDeleteApiView
from rrhh.cargos.views.list_view import CargoListApiView
from rrhh.cargos.views.update_view import CargoUpdateApiView

urlpatterns = [
    path(
        "",
        CargoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        CargoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        CargoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        CargoDeleteApiView.as_view(),
        name="delete",
    ),
]
