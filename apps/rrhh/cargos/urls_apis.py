from django.urls import path

from .views.create_view import CargoCreateApiView
from .views.delete_view import CargoDeleteApiView
from .views.list_view import CargoListApiView
from .views.update_view import CargoUpdateApiView

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
