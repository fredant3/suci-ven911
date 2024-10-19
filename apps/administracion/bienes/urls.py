from django.urls import path

from .views.create_view import BienCreateView
from .views.delete_view import BienDeleteView
from .views.list_view import BienListView
from .views.update_view import BienUpdateView

urlpatterns = [
    path(
        "",
        BienListView.as_view(),
        name="list",
    ),
    path(
        "create",
        BienCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        BienListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        BienUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        BienDeleteView.as_view(),
        name="delete",
    ),
]
