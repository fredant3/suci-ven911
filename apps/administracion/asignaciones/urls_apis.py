from administracion.averia.views.create_view import AveriaCreateApiView
from administracion.averia.views.delete_view import AveriaDeleteApiView
from administracion.averia.views.update_view import AveriaUpdateApiView
from django.urls import path

urlpatterns = [
    path(
        "",
        name="list",
    ),
    path(
        "create",
        AveriaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        AveriaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        AveriaDeleteApiView.as_view(),
        name="delete",
    ),
]
