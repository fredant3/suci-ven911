from django.urls import path

from tecnologia.views.create_view import TecnologiaCreateApiView
from tecnologia.views.delete_view import TecnologiaDeleteApiView
from tecnologia.views.list_view import TecnologiaListApiView
from tecnologia.views.update_view import TecnologiaUpdateApiView

urlpatterns = [
    path(
        "",
        TecnologiaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        TecnologiaCreateApiView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        TecnologiaUpdateApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TecnologiaDeleteApiView.as_view(),
        name="delete",
    ),
]
