from django.urls import path
from gestion_comunicacional.views.create_view import GestioncomunicacionalCreateView
from gestion_comunicacional.views.delete_view import GestioncomunicacionalDeleteApiView
from gestion_comunicacional.views.list_view import GestioncomunicacionalListApiView
from gestion_comunicacional.views.update_view import GestioncomunicacionalUpdateApiView

urlpatterns = [
    path(
        "",
        GestioncomunicacionalDeleteApiView.as_view(),
        name="list",
    ),
    path(
        "create",
        GestioncomunicacionalCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/update",
        GestioncomunicacionalListApiView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        GestioncomunicacionalUpdateApiView.as_view(),
        name="delete",
    ),
]
