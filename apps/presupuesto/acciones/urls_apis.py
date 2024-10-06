from django.urls import path

from .views.create_view import AccionCreateApiView
from .views.delete_view import AccionDeleteApiView
from .views.export_view import AccionPDFView
from .views.list_view import AccionListApiView
from .views.update_view import AccionUpdateApiView

urlpatterns = [
    path(
        "",
        AccionListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        AccionCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        AccionUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        AccionDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export/pdf",
        AccionPDFView.as_view(),
        name="export_pdf",
    ),
]
