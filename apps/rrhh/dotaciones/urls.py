from django.urls import path

from rrhh.dotaciones.views.create_view import DotacionCreateView
from rrhh.dotaciones.views.delete_view import DotacionDeleteView
from rrhh.dotaciones.views.list_view import DotacionListView
from rrhh.dotaciones.views.update_view import DotacionUpdateView
from rrhh.dotaciones.views.export_view import DotacionExcelView

urlpatterns = [
    path(
        "",
        DotacionListView.as_view(),
        name="list",
    ),
    path(
        "create",
        DotacionCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        DotacionListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        DotacionUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        DotacionDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export/excel",
        DotacionExcelView.as_view(),
        name="export_excel",
    ),
]
