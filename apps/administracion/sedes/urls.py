from django.urls import path

from .views.create_view import SedeCreateView
from .views.delete_view import SedeDeleteView
from .views.list_view import SedeListView
from .views.update_view import SedeUpdateView

urlpatterns = [
    path(
        "",
        SedeListView.as_view(),
        name="list",
    ),
    path(
        "create",
        SedeCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        SedeListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        SedeUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        SedeDeleteView.as_view(),
        name="delete",
    ),
]
