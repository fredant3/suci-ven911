from django.urls import path

from .views.create_view import ReceptorCreateApiView
from .views.delete_view import ReceptorDeleteApiView
from .views.export_view import ReceptorPDFView
from .views.list_view import ReceptorListApiView
from .views.update_view import ReceptorUpdateApiView

urlpatterns = [
    path(
        "",
        ReceptorListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        ReceptorCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        ReceptorUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ReceptorDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export/pdf",
        ReceptorPDFView.as_view(),
        name="export_pdf",
    ),
]
