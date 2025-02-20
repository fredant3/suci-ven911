from django.urls import path

from rrhh.empleados.views.create_view import EmpleadoCreateView
from rrhh.empleados.views.delete_view import EmpleadoDeleteView
from rrhh.empleados.views.list_view import EmpleadoListView
from rrhh.empleados.views.update_view import EmpleadoUpdateView

urlpatterns = [
    path(
        "",
        EmpleadoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        EmpleadoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        EmpleadoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        EmpleadoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        EmpleadoDeleteView.as_view(),
        name="delete",
    ),
]
