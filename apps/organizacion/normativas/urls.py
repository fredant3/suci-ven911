from django.urls import path

from .views.create_view import NormativaCreateView
from .views.delete_view import NormativaDeleteView
from .views.list_view import NormativaListView
from .views.update_view import NormativaUpdateView

urlpatterns = [
    path(
        "",
        NormativaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        NormativaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        NormativaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        NormativaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        NormativaDeleteView.as_view(),
        name="delete",
    ),
]
