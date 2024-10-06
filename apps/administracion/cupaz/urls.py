from django.urls import path

from .views.create_view import CuadrantePazCreateView
from .views.delete_view import CuadrantePazDeleteView
from .views.list_view import CuadrantePazListView
from .views.update_view import CuadrantePazUpdateView

urlpatterns = [
    path(
        "",
        CuadrantePazListView.as_view(),
        name="list",
    ),
    path(
        "create",
        CuadrantePazCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        CuadrantePazListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        CuadrantePazUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        CuadrantePazDeleteView.as_view(),
        name="delete",
    ),
]
