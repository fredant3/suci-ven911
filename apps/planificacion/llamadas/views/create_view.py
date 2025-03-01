from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController
from planificacion.llamadas.forms import LlamadaForm
from planificacion.llamadas.services import LlamadaService

from templates.sneat import TemplateLayout


class LlamadaCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = "planificacion.llamadas.agregar_llamada"
    form_class = LlamadaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Planificación"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Planificación"
        context["submodule"] = "Llamadas"
        context["titleForm"] = "Añadir una llamada"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("llamadas:list")
        context["urlForm"] = reverse_lazy("api_llamadas:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class LlamadaCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = "planificacion.llamadas.agregar_llamada"
    form_class = LlamadaForm

    def __init__(self):
        self.service = LlamadaService()
