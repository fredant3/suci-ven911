from django.urls import path

from rrhh.dotaciones.views.create_view import DotacionCreateApiView
from rrhh.dotaciones.views.delete_view import DotacionDeleteApiView
from rrhh.dotaciones.views.list_view import DotacionListApiView
from rrhh.dotaciones.views.update_view import DotacionUpdateApiView
from rrhh.dotaciones.views.export_view import DotacionExcelView

urlpatterns = [
    path(
        "",
        DotacionListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        DotacionCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        DotacionUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        DotacionDeleteApiView.as_view(),
        name="delete",
    ),
    path(
        "export/excel",
        DotacionExcelView.as_view(),
        name="export_excel",
    ),
]
