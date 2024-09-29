from django.urls import path

from .views.create_view import ActividadCreateApiView
from .views.delete_view import ActividadDeleteApiView
from .views.list_view import ActividadListApiView
from .views.update_view import ActividadUpdateApiView

urlpatterns = [
    path(
        "",
        ActividadListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        ActividadCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        ActividadUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ActividadDeleteApiView.as_view(),
        name="delete",
    ),
]
