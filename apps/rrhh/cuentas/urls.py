from django.urls import path

from .views.create_view import CuentaCreateView
from .views.delete_view import CuentaDeleteView
from .views.list_view import CuentaListView
from .views.update_view import CuentaUpdateView

urlpatterns = [
    path(
        "",
        CuentaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        CuentaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        CuentaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        CuentaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        CuentaDeleteView.as_view(),
        name="delete",
    ),
]
