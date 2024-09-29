from django.urls import path

from .views.create_view import ObjetivoCreateView
from .views.delete_view import ObjetivoDeleteView
from .views.list_view import ObjetivoListView
from .views.update_view import ObjetivoUpdateView

urlpatterns = [
    path(
        "",
        ObjetivoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        ObjetivoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        ObjetivoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        ObjetivoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ObjetivoDeleteView.as_view(),
        name="delete",
    ),
]
