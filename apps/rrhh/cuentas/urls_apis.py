from django.urls import path

from .views.create_view import CuentaCreateApiView
from .views.delete_view import CuentaDeleteApiView
from .views.list_view import CuentaListApiView
from .views.update_view import CuentaUpdateApiView

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
