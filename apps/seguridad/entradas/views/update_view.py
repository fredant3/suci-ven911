from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import EntradaForm
from ..models import Entrada
from ..services import EntradaService


class EntradaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = EntradaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Entradas"
        context["titleForm"] = "Actualizar entrada"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("entradas:list")
        context["urlForm"] = reverse_lazy(
            "api_entradas:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Entrada.objects.filter(pk=id)


class EntradaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = EntradaForm

    def __init__(self):
        self.service = EntradaService()
