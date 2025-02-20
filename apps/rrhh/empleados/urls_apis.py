from django.urls import path

from rrhh.empleados.views.create_view import EmpleadoCreateApiView
from rrhh.empleados.views.delete_view import EmpleadoDeleteApiView
from rrhh.empleados.views.list_view import EmpleadoListApiView
from rrhh.empleados.views.update_view import EmpleadoUpdateApiView

urlpatterns = [
    path(
        "",
        EmpleadoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        EmpleadoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        EmpleadoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        EmpleadoDeleteApiView.as_view(),
        name="delete",
    ),
]
