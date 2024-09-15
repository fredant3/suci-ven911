from django.urls import path

from .views import DenunciaListApiView

urlpatterns = [
    path(
        "",
        DenunciaListApiView.as_view(),
        name="list",
    ),
]
