from django.urls import path

from potencia.uri.views.create_view import UriCreateApiView
from potencia.uri.views.delete_view import UriDeleteApiView
from potencia.uri.views.list_view import UriListApiView
from potencia.uri.views.update_view import UriUpdateApiView

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
