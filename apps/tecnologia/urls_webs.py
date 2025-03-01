from django.urls import path
from tecnologia.views.list_view import TecnologiaListView

urlpatterns = [
    path(
        "",
        TecnologiaListView.as_view(),
        name="list",
    ),
    path(
        "<int:pk>/read",
        TecnologiaListView.as_view(),
        name="read",
    ),
    path("<int:pk>/update", TecnologiaListView.as_view(), name="update"),
]
