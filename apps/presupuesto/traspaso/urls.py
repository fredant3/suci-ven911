from django.urls import path

from presupuesto.traspaso.views.create_view import TraspasoReceptorWizardView
from presupuesto.traspaso.views.delete_view import TraspasoDeleteView
from presupuesto.traspaso.views.list_view import TraspasoListView
from presupuesto.traspaso.views.update_view import TraspasoUpdateView

urlpatterns = [
    path(
        "",
        TraspasoListView.as_view(),
        name="list",
    ),
    path(
        "create",
        TraspasoReceptorWizardView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        TraspasoListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        TraspasoUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        TraspasoDeleteView.as_view(),
        name="delete",
    ),
]
