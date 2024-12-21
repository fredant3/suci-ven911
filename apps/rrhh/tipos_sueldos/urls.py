from django.urls import path

from rrhh.tipos_sueldos.views.create_view import TipoSueldoCreateView
from rrhh.tipos_sueldos.views.delete_view import TipoSueldoDeleteView
from rrhh.tipos_sueldos.views.list_view import TipoSueldoListView
from rrhh.tipos_sueldos.views.update_view import TipoSueldoUpdateView

urlpatterns = [
    path(
        "",
        TipoSueldoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        TipoSueldoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        TipoSueldoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        TipoSueldoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TipoSueldoDeleteView.as_view(),
        name="delete",
    ),
]
