from django.urls import path

from .views.create_view import GestionCreateApiView
from .views.delete_view import GestionDeleteApiView
from .views.list_view import GestionListApiView
from .views.update_view import GestionUpdateApiView

urlpatterns = [
    path(
        "",
        GestionListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        GestionCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        GestionUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        GestionDeleteApiView.as_view(),
        name="delete",
    ),
]
