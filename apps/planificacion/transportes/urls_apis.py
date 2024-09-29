from django.urls import path

from .views.create_view import TransporteCreateApiView
from .views.delete_view import TransporteDeleteApiView
from .views.list_view import TransporteListApiView
from .views.update_view import TransporteUpdateApiView

urlpatterns = [
    path(
        "",
        TransporteListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        TransporteCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        TransporteUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TransporteDeleteApiView.as_view(),
        name="delete",
    ),
]
