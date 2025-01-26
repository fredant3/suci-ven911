from django.urls import path

from .views.create_view import EducacionCreateApiView
from .views.delete_view import EducacionDeleteApiView
from .views.list_view import EducacionListApiView
from .views.update_view import EducacionUpdateApiView

urlpatterns = [
    path(
        "",
        EducacionListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        EducacionCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        EducacionUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        EducacionDeleteApiView.as_view(),
        name="delete",
    ),
]
