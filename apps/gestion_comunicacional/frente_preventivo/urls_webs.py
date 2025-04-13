from django.urls import path
from gestion_comunicacional.frente_preventivo.views.create_view import (
    FrentePreventivoCreateView,
)
from gestion_comunicacional.frente_preventivo.views.delete_view import (
    FrentePreventivoDeleteView,
)
from gestion_comunicacional.frente_preventivo.views.list_view import (
    FrentePreventivoListView,
)
from gestion_comunicacional.frente_preventivo.views.update_view import (
    FrentePreventivoUpdateView,
)


urlpatterns = [
    path("", FrentePreventivoListView.as_view(), name="list"),
    path("create", FrentePreventivoCreateView.as_view(), name="create"),
    path("<int:pk>/read", FrentePreventivoListView.as_view(), name="read"),
    path("<int:pk>/update", FrentePreventivoUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", FrentePreventivoDeleteView.as_view(), name="delete"),
]
