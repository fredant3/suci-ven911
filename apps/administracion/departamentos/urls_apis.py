from django.urls import path

from .views.create_view import DepartamentoCreateApiView
from .views.delete_view import DepartamentoDeleteApiView
from .views.list_view import DepartamentoListApiView
from .views.update_view import DepartamentoUpdateApiView

urlpatterns = [
    path(
        "",
        DepartamentoListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        DepartamentoCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        DepartamentoUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        DepartamentoDeleteApiView.as_view(),
        name="delete",
    ),
]
