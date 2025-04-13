from django.urls import path
from gestion_comunicacional.frente_preventivo.views.create_view import (
    FrentePreventivoCreateApiView,
)
from gestion_comunicacional.frente_preventivo.views.delete_view import (
    FrentePreventivoDeleteApiView,
)
from gestion_comunicacional.frente_preventivo.views.list_view import (
    FrentePreventivoListApiView,
)
from gestion_comunicacional.frente_preventivo.views.update_view import (
    FrentePreventivoUpdateApiView,
)

urlpatterns = [
    path(
        "",
        FrentePreventivoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        FrentePreventivoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        FrentePreventivoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        FrentePreventivoDeleteApiView.as_view(),
        name="delete",
    ),
]
