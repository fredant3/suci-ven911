from django.urls import path

from .views.create_view import AccionCreateView
from .views.delete_view import AccionDeleteView
from .views.list_view import AccionListView
from .views.update_view import AccionUpdateView

urlpatterns = [
    path(
        "",
        AccionListView.as_view(),
        name="list",
    ),
    path(
        "create",
        AccionCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        AccionListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        AccionUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        AccionDeleteView.as_view(),
        name="delete",
    ),
]
