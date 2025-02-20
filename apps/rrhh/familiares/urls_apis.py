from django.urls import path

from rrhh.familiares.views.create_view import FamiliarCreateApiView
from rrhh.familiares.views.delete_view import FamiliarDeleteApiView
from rrhh.familiares.views.list_view import FamiliarListApiView
from rrhh.familiares.views.update_view import FamiliarUpdateApiView

urlpatterns = [
    path(
        "",
        FamiliarListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        FamiliarCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        FamiliarUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        FamiliarDeleteApiView.as_view(),
        name="delete",
    ),
]
