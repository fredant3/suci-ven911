from django.urls import path
from potencia.uri.views.create_view import UriCreateView
from potencia.uri.views.delete_view import UriDeleteView
from potencia.uri.views.list_view import UriListView
from potencia.uri.views.update_view import UriUpdateView

urlpatterns = [
    path(
        "",
        UriListView.as_view(),
        name="list",
    ),
    path(
        "create",
        UriCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        UriListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        UriUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        UriDeleteView.as_view(),
        name="delete",
    ),
]
