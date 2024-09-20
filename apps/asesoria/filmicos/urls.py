from django.urls import path

from .views.create_view import RegistroFilmicoCreateView
from .views.delete_view import RegistroFilmicoDeleteView
from .views.list_view import RegistroFilmicoListView
from .views.update_view import RegistroFilmicoUpdateView

urlpatterns = [
    path(
        "",
        RegistroFilmicoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        RegistroFilmicoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        RegistroFilmicoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        RegistroFilmicoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        RegistroFilmicoDeleteView.as_view(),
        name="delete",
    ),
]
