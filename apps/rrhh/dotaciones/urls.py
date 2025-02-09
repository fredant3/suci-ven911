from django.urls import path

from .views.create_view import DotacionCreateView
from .views.delete_view import DotacionDeleteView
from .views.list_view import DotacionListView
from .views.update_view import DotacionUpdateView

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
]
