from django.urls import path

from .views.create_view import IncidenciaCreateView
from .views.delete_view import IncidenciaDeleteView
from .views.list_view import IncidenciaListView
from .views.update_view import IncidenciaUpdateView

urlpatterns = [
    path(
        "",
        IncidenciaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        IncidenciaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        IncidenciaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        IncidenciaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        IncidenciaDeleteView.as_view(),
        name="delete",
    ),
]
