from django.urls import path

from .views.create_view import CedenteCreateApiView
from .views.delete_view import CedenteDeleteApiView
from .views.export_view import CedentePDFView
from .views.list_view import CedenteListApiView
from .views.update_view import CedenteUpdateApiView

urlpatterns = [
    path(
        "",
        CedenteListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        CedenteCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        CedenteUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        CedenteDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export/pdf",
        CedentePDFView.as_view(),
        name="export_pdf",
    ),
]
