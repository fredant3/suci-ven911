from django.urls import path

from presupuesto.proyecto.views.create_view import ProyectoCreateApiView
from presupuesto.proyecto.views.delete_view import ProyectoDeleteApiView
from presupuesto.proyecto.views.export_view import ProyectoPDFView
from presupuesto.proyecto.views.list_view import ProyectoListApiView
from presupuesto.proyecto.views.update_view import ProyectoUpdateApiView

urlpatterns = [
    path(
        "",
        ProyectoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        ProyectoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        ProyectoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ProyectoDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export/pdf",
        ProyectoPDFView.as_view(),
        name="export_pdf",
    ),
]
