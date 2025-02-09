from django.urls import path
from tecnologia.views.create_view import TecnologiaCreateView
from tecnologia.views.delete_view import TecnologiaDeleteView
from tecnologia.views.list_view import TecnologiaListView
from tecnologia.views.update_view import TecnologiaUpdateView

urlpatterns = [
    path(
        "",
        TecnologiaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        TecnologiaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        TecnologiaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        TecnologiaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TecnologiaDeleteView.as_view(),
        name="delete",
    ),
]
