from django.urls import path

from .views.create_view import TipoEmpleadoCreateView
from .views.delete_view import TipoEmpleadoDeleteView
from .views.list_view import TipoEmpleadoListView
from .views.update_view import TipoEmpleadoUpdateView

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
]
