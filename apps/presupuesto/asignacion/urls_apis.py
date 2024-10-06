from django.urls import path

from .views.create_view import AsignacionCreateApiView
from .views.delete_view import AsignacionDeleteApiView
from .views.export_view import AsignacionPDFView
from .views.list_view import AsignacionListApiView
from .views.update_view import AsignacionUpdateApiView

urlpatterns = [
    path(
        "",
        AsignacionListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        AsignacionCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        AsignacionUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        AsignacionDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export/pdf",
        AsignacionPDFView.as_view(),
        name="export_pdf",
    ),
]
