from django.urls import path

from .views.create_view import ContratoCreateApiView
from .views.delete_view import ContratoDeleteApiView
from .views.list_view import ContratoListApiView
from .views.update_view import ContratoUpdateApiView

urlpatterns = [
    path(
        "",
        ContratoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        ContratoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        ContratoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ContratoDeleteApiView.as_view(),
        name="delete",
    ),
]
