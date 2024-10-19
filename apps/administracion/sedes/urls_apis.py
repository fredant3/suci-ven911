from django.urls import path

from .views.create_view import SedeCreateApiView
from .views.delete_view import SedeDeleteApiView
from .views.list_view import SedeListApiView
from .views.update_view import SedeUpdateApiView

urlpatterns = [
    path(
        "",
        SedeListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        SedeCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        SedeUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        SedeDeleteApiView.as_view(),
        name="delete",
    ),
]
