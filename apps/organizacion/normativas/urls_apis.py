from django.urls import path

from .views.create_view import NormativaCreateApiView
from .views.delete_view import NormativaDeleteApiView
from .views.list_view import NormativaListApiView
from .views.update_view import NormativaUpdateApiView

urlpatterns = [
    path(
        "",
        NormativaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        NormativaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        NormativaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        NormativaDeleteApiView.as_view(),
        name="delete",
    ),
]
