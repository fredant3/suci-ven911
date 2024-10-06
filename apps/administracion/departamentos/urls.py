from django.urls import path

from .views.create_view import DepartamentoCreateView
from .views.delete_view import DepartamentoDeleteView
from .views.list_view import DepartamentoListView
from .views.update_view import DepartamentoUpdateView

urlpatterns = [
    path(
        "",
        DepartamentoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        DepartamentoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        DepartamentoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        DepartamentoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        DepartamentoDeleteView.as_view(),
        name="delete",
    ),
]
