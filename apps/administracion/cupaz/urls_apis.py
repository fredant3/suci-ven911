from django.urls import path

from .views.create_view import CuadrantePazCreateApiView
from .views.delete_view import CuadrantePazDeleteApiView
from .views.list_view import CuadrantePazListApiView
from .views.update_view import CuadrantePazUpdateApiView

urlpatterns = [
    path(
        "",
        CuadrantePazListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        CuadrantePazCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        CuadrantePazUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        CuadrantePazDeleteApiView.as_view(),
        name="delete",
    ),
]
