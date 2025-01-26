from django.urls import path
from planificacion.llamadas.views.create_view import LlamadaCreateApiView
from planificacion.llamadas.views.delete_view import LlamadaDeleteApiView
from planificacion.llamadas.views.list_view import LlamadaListApiView
from planificacion.llamadas.views.update_view import LlamadaUpdateApiView

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
