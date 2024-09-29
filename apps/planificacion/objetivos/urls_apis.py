from django.urls import path

from .views.create_view import ObjetivoCreateApiView
from .views.delete_view import ObjetivoDeleteApiView
from .views.list_view import ObjetivoListApiView
from .views.update_view import ObjetivoUpdateApiView

urlpatterns = [
    path(
        "",
        ObjetivoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        ObjetivoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        ObjetivoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ObjetivoDeleteApiView.as_view(),
        name="delete",
    ),
]
