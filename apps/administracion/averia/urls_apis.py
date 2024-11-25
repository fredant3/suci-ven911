from administracion.averia.views.create_view import AveriaCreateView
from django.urls import path
from administracion.averia.views.delete_view import AveriaDeleteApiView
from administracion.averia.views.list_view import AveriaListApiView
from administracion.averia.views.update_view import AveriaUpdateApiView

urlpatterns = [
    path(
        "",
        AveriaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        AveriaCreateView.as_view(),
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
