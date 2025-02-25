from django.urls import path
from tecnologia.views.list_view import TecnologiaListApiView

urlpatterns = [
    path(
        "",
        TecnologiaListApiView.as_view(),
        name="list",
    ),
    path(
        "<int:pk>/read",
        TecnologiaListApiView.as_view(),
        name="read",
    ),
]
