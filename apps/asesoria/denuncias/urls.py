from django.urls import path

from .views.create_view import DenunciaCreateView
from .views.delete_view import DenunciaDeleteView
from .views.list_view import DenunciaListView
from .views.update_view import DenunciaUpdateView

urlpatterns = [
    path(
        "",
        DenunciaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        DenunciaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        DenunciaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        DenunciaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        DenunciaDeleteView.as_view(),
        name="delete",
    ),
]
