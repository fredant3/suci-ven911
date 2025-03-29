from django.urls import path

from potencia.uri.view.create_view import UriCreateApiView
from potencia.uri.view.delete_view import UriDeleteApiView
from potencia.uri.view.list_view import UriListApiView
from potencia.uri.view.update_view import UriUpdateApiView

urlpatterns = [
    path(
        "",
        UriListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        UriCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        UriUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        UriDeleteApiView.as_view(),
        name="delete",
    ),
]
