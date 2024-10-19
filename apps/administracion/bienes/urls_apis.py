from django.urls import path

from .views.create_view import BienCreateApiView
from .views.delete_view import BienDeleteApiView
from .views.list_view import BienListApiView
from .views.update_view import BienUpdateApiView

urlpatterns = [
    path(
        "",
        BienListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        BienCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        BienUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        BienDeleteApiView.as_view(),
        name="delete",
    ),
]
