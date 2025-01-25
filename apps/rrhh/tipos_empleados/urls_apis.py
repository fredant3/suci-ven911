from django.urls import path

from .views.create_view import TipoEmpleadoCreateApiView
from .views.delete_view import TipoEmpleadoDeleteApiView
from .views.list_view import TipoEmpleadoListApiView
from .views.update_view import TipoEmpleadoUpdateApiView

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
]
