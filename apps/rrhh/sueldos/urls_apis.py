from django.urls import path

from .views.create_view import SueldoCreateApiView
from .views.delete_view import SueldoDeleteApiView
from .views.list_view import SueldoListApiView
from .views.update_view import SueldoUpdateApiView

urlpatterns = [
    path(
        "",
        SueldoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        SueldoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        SueldoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        SueldoDeleteApiView.as_view(),
        name="delete",
    ),
]
