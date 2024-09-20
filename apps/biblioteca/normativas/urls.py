from django.urls import path

from .views.delete_view import DenunciaDeleteView
from .views.list_view import NormativaListView

urlpatterns = [
    path(
        "",
        NormativaListView.as_view(),
        name="list",
    ),
    path(
        "<int:pk>/read",
        DenunciaListView.as_view(),
        name="read",
    ),
]
