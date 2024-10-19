from django.urls import path

from .views.create_view import EntradaCreateView
from .views.delete_view import EntradaDeleteView
from .views.list_view import EntradaListView
from .views.update_view import EntradaUpdateView

urlpatterns = [
    path(
        "",
        EntradaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        EntradaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        EntradaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        EntradaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        EntradaDeleteView.as_view(),
        name="delete",
    ),
]
