from django.urls import path

from .views.create_view import CargoCreateView
from .views.delete_view import CargoDeleteView
from .views.list_view import CargoListView
from .views.update_view import CargoUpdateView

urlpatterns = [
    path(
        "",
        CargoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        CargoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        CargoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        CargoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        CargoDeleteView.as_view(),
        name="delete",
    ),
]
