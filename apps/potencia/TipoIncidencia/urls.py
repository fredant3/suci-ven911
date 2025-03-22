from potencia.tipoIncidencia.views.create_view import TipoIncidenciaCreateView
from potencia.tipoIncidencia.views.delete_view import TipoIncidenciaDeleteView
from potencia.tipoIncidencia.views.list_view import TipoIncidenciaListView
from potencia.tipoIncidencia.views.update_view import TipoIncidenciaUpdateView
from django.urls import path

urlpatterns = [
    path(
        "",
        TipoIncidenciaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        TipoIncidenciaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        TipoIncidenciaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        TipoIncidenciaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TipoIncidenciaDeleteView.as_view(),
        name="delete",
    ),
]
