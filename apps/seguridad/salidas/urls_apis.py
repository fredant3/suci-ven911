from django.urls import path

from .views.create_view import SalidaCreateApiView
from .views.delete_view import SalidaDeleteApiView
from .views.list_view import SalidaListApiView
from .views.update_view import SalidaUpdateApiView

urlpatterns = [
    path(
        "",
        SalidaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        SalidaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        SalidaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        SalidaDeleteApiView.as_view(),
        name="delete",
    ),
]
