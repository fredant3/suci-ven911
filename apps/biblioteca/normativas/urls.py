from django.urls import path

from .views.list_view import NormativaListView

urlpatterns = [
    path(
        "",
        NormativaListView.as_view(),
        name="list",
    ),
]
