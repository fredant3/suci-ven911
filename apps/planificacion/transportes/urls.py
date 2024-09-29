from django.urls import path

from .views.create_view import TransporteCreateView
from .views.delete_view import TransporteDeleteView
from .views.list_view import TransporteListView
from .views.update_view import TransporteUpdateView

urlpatterns = [
    path(
        "",
        TransporteListView.as_view(),
        name="list",
    ),
    path(
        "create",
        TransporteCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        TransporteListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        TransporteUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TransporteDeleteView.as_view(),
        name="delete",
    ),
]
