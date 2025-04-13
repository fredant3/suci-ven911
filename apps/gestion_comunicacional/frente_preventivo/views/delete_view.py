from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from gestion_comunicacional.frente_preventivo.forms import FrentePreventivoForm
from gestion_comunicacional.frente_preventivo.models import FrentePreventivo
from gestion_comunicacional.frente_preventivo.services import FrentePreventivoService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class FrentePreventivoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "frentepreventivo.eliminar_frentepreventivo"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Frente Preventivo"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Frente Preventivo"
        context["submodule"] = "Frente Preventivo"
        context["titleForm"] = "Eliminar frente preventivo"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("frente preventivo:list")
        context["urlDelete"] = reverse_lazy(
            "api_frente preventivo:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return FrentePreventivo.objects.filter(pk=id)


class FrentePreventivoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "frentepreventivo.eliminar_frentepreventivo"
    form_class = FrentePreventivoForm

    def __init__(self):
        self.service = FrentePreventivoService()
