from django.urls import path

from .views.create_view import EducacionCreateView
from .views.delete_view import EducacionDeleteView
from .views.list_view import EducacionListView
from .views.update_view import EducacionUpdateView

urlpatterns = [
    path(
        "",
        EducacionListView.as_view(),
        name="list",
    ),
    path(
        "create",
        EducacionCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        EducacionListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        EducacionUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        EducacionDeleteView.as_view(),
        name="delete",
    ),
]
