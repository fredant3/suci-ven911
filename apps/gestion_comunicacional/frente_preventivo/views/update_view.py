from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from gestion_comunicacional.frente_preventivo.forms import FrentePreventivoForm
from gestion_comunicacional.frente_preventivo.models import FrentePreventivo
from gestion_comunicacional.frente_preventivo.services import FrentePreventivoService


class FrentePreventivoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "frentepreventivo.actualizar_frentepreventivo"
    form_class = FrentePreventivoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Frente Preventivo"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Frente Preventivo"
        context["submodule"] = "Frente Preventivo"
        context["titleForm"] = "Actualizar frente preventivo"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("frente preventivo:list")
        context["urlForm"] = reverse_lazy(
            "api_frente preventivo:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return FrentePreventivo.objects.filter(pk=id)


class FrentePreventivoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "frentepreventivo.actualizar_frentepreventivo"
    form_class = FrentePreventivoForm

    def __init__(self):
        self.service = FrentePreventivoService()
