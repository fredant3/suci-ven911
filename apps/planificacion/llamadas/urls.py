from django.urls import path
from planificacion.llamadas.views.create_view import LlamadaCreateView
from planificacion.llamadas.views.delete_view import LlamadaDeleteView
from planificacion.llamadas.views.list_view import LlamadaListView
from planificacion.llamadas.views.update_view import LlamadaUpdateView

urlpatterns = [
    path(
        "",
        LlamadaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        LlamadaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        LlamadaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        LlamadaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        LlamadaDeleteView.as_view(),
        name="delete",
    ),
]
