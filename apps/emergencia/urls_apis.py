from django.urls import path

from .views.create_view import EmergenciaCreateApiView
from .views.delete_view import EmergenciaDeleteApiView
from .views.list_view import EmergenciaListApiView
from .views.update_view import EmergenciaUpdateApiView

urlpatterns = [
    path(
        "",
        EmergenciaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        EmergenciaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        EmergenciaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        EmergenciaDeleteApiView.as_view(),
        name="delete",
    ),
]
