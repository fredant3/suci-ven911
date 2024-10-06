from django.urls import path

from .views.create_view import GestionCreateView
from .views.delete_view import GestionDeleteView
from .views.list_view import GestionListView
from .views.update_view import GestionUpdateView

urlpatterns = [
    path(
        "",
        GestionListView.as_view(),
        name="list",
    ),
    path(
        "create",
        GestionCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        GestionListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        GestionUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        GestionDeleteView.as_view(),
        name="delete",
    ),
]
