from django.urls import path

from .views.create_view import TipoSueldoCreateApiView
from .views.delete_view import TipoSueldoDeleteApiView
from .views.list_view import TipoSueldoListApiView
from .views.update_view import TipoSueldoUpdateApiView

urlpatterns = [
    path(
        "",
        TipoSueldoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        TipoSueldoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        TipoSueldoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TipoSueldoDeleteApiView.as_view(),
        name="delete",
    ),
]
