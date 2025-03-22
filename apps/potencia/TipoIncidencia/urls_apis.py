from potencia.tipoIncidencia.views.create_view import TipoIncidenciaCreateApiView
from potencia.tipoIncidencia.views.delete_view import TipoIncidenciaDeleteApiView
from potencia.tipoIncidencia.views.list_view import TipoIncidenciaListApiView
from potencia.tipoIncidencia.views.update_view import TipoIncidenciaUpdateApiView
from django.urls import path

urlpatterns = [
    path(
        "",
        TipoIncidenciaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        TipoIncidenciaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        TipoIncidenciaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TipoIncidenciaDeleteApiView.as_view(),
        name="delete",
    ),
]
