from django.urls import path

from .views.create_view import VehiculoCreateApiView
from .views.delete_view import VehiculoDeleteApiView
from .views.list_view import VehiculoListApiView
from .views.update_view import VehiculoUpdateApiView

urlpatterns = [
    path(
        "",
        VehiculoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        VehiculoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        VehiculoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        VehiculoDeleteApiView.as_view(),
        name="delete",
    ),
]
