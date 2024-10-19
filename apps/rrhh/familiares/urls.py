from django.urls import path

from .views.create_view import FamiliarCreateView
from .views.delete_view import FamiliarDeleteView
from .views.list_view import FamiliarListView
from .views.update_view import FamiliarUpdateView

urlpatterns = [
    path(
        "",
        FamiliarListView.as_view(),
        name="list",
    ),
    path(
        "create",
        FamiliarCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        FamiliarListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        FamiliarUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        FamiliarDeleteView.as_view(),
        name="delete",
    ),
]
