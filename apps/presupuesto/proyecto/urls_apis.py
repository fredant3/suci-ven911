from django.urls import path

from .views.create_view import ProyectoCreateApiView
from .views.delete_view import ProyectoDeleteApiView
from .views.export_view import ProyectoPDFView
from .views.list_view import ProyectoListApiView
from .views.update_view import ProyectoUpdateApiView

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
