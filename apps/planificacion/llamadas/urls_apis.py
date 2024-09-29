from django.urls import path

from .views.create_view import LlamadaCreateApiView
from .views.delete_view import LlamadaDeleteApiView
from .views.list_view import LlamadaListApiView
from .views.update_view import LlamadaUpdateApiView

urlpatterns = [
    path(
        "",
        LlamadaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        LlamadaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        LlamadaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        LlamadaDeleteApiView.as_view(),
        name="delete",
    ),
]
