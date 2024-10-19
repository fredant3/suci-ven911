from django.urls import path

from .views.create_view import EntradaCreateApiView
from .views.delete_view import EntradaDeleteApiView
from .views.list_view import EntradaListApiView
from .views.update_view import EntradaUpdateApiView

urlpatterns = [
    path(
        "",
        EntradaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        EntradaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        EntradaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        EntradaDeleteApiView.as_view(),
        name="delete",
    ),
]
