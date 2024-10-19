from django.urls import path

from .views.create_view import CedenteCreateView
from .views.delete_view import CedenteDeleteView
from .views.list_view import CedenteListView
from .views.update_view import CedenteUpdateView

urlpatterns = [
    path(
        "",
        CedenteListView.as_view(),
        name="list",
    ),
    path(
        "create",
        CedenteCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        CedenteListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        CedenteUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        CedenteDeleteView.as_view(),
        name="delete",
    ),
]
