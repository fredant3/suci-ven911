from administracion.compras.views.create_view import ComprasCreateApiView
from administracion.compras.views.delete_view import CompraDeleteApiView
from administracion.compras.views.list_view import ComprasListApiView
from administracion.compras.views.update_view import ComprasUpdateApiView
from django.urls import path

urlpatterns = [
    path(
        "",
        ComprasListApiView.as_view(),
        name="list",
    ),
    path(
        "create/<str:type>/",
        ComprasCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        ComprasUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        CompraDeleteApiView.as_view(),
        name="delete",
    ),
]
