from django.urls import path

from rrhh.educaciones.views.create_view import EducacionCreateView
from rrhh.educaciones.views.delete_view import EducacionDeleteView
from rrhh.educaciones.views.list_view import EducacionListView
from rrhh.educaciones.views.update_view import EducacionUpdateView
from rrhh.educaciones.views.export_view import EducacionExcelView

urlpatterns = [
    path(
        "",
        EducacionListView.as_view(),
        name="list",
    ),
    path(
        "create",
        EducacionCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        EducacionListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        EducacionUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        EducacionDeleteView.as_view(),
        name="delete",
    ),
    path(
        "export/excel",
        EducacionExcelView.as_view(),
        name="export_excel",
    ),
]
