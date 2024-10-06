from django.urls import path

from .views.create_view import ContratoCreateView
from .views.delete_view import ContratoDeleteView
from .views.list_view import ContratoListView
from .views.update_view import ContratoUpdateView

urlpatterns = [
    path(
        "",
        ContratoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        ContratoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        ContratoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        ContratoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ContratoDeleteView.as_view(),
        name="delete",
    ),
]
