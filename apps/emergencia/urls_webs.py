from django.urls import path
from emergencia.views.create_view import EmergenciaCreateView
from emergencia.views.delete_view import EmergenciaDeleteView
from emergencia.views.list_view import EmergenciaListView
from emergencia.views.update_view import EmergenciaUpdateView

urlpatterns = [
    path(
        "",
        EmergenciaListView.as_view(),
        name="list",
    ),
    path(
        "create",
        EmergenciaCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        EmergenciaListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        EmergenciaUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        EmergenciaDeleteView.as_view(),
        name="delete",
    ),
]
