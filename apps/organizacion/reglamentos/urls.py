from django.urls import path

from .views.create_view import ReglamentoCreateView
from .views.delete_view import ReglamentoDeleteView
from .views.list_view import ReglamentoListView
from .views.update_view import ReglamentoUpdateView

urlpatterns = [
    path(
        "",
        ReglamentoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        ReglamentoCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        ReglamentoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        ReglamentoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ReglamentoDeleteView.as_view(),
        name="delete",
    ),
]
