from django.urls import path

from .views.create_view import DenunciaCreateView
from .views.list_view import DenunciaListApiView

urlpatterns = [
    path(
        "",
        DenunciaListApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        DenunciaCreateView.as_view(),
        name="create",
    ),
]
