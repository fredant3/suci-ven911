from django.urls import path

from .views.create_view import DenunciaCreateApiView
from .views.list_view import DenunciaListApiView
from .views.update_view import DenunciaUpdateApiView

urlpatterns = [
    path(
        "",
        DenunciaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        DenunciaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        DenunciaUpdateApiView.as_view(),
        name="update",
    ),
]
