from django.urls import path
from planificacion.infraestructuras.views.create_view import InfraestructuraCreateView
from planificacion.infraestructuras.views.delete_view import InfraestructuraDeleteView
from planificacion.infraestructuras.views.list_view import InfraestructuraListView
from planificacion.infraestructuras.views.update_view import InfraestructuraUpdateView

urlpatterns = [
    path(
        "",
        InfraestructuraListView.as_view(),
        name="list",
    ),
    path(
        "create",
        InfraestructuraCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        InfraestructuraListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        InfraestructuraUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        InfraestructuraDeleteView.as_view(),
        name="delete",
    ),
]
