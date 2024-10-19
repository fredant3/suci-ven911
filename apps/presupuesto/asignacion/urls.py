from django.urls import path

from .views.create_view import AsignacionCreateView
from .views.delete_view import AsignacionDeleteView
from .views.list_view import AsignacionListView
from .views.update_view import AsignacionUpdateView

urlpatterns = [
    path(
        "",
        AsignacionListView.as_view(),
        name="list",
    ),
    path(
        "create",
        AsignacionCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        AsignacionListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        AsignacionUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        AsignacionDeleteView.as_view(),
        name="delete",
    ),
]
