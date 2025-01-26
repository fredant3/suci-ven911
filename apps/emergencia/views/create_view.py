from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from emergencia.forms import EmergenciaForm
from emergencia.services import EmergenciaService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout


class EmergenciaCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = EmergenciaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Emergencias"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Emergencias"
        context["submodule"] = "Emergencias"
        context["titleForm"] = "Añadir una emergencia"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("emergencias:list")
        context["urlForm"] = reverse_lazy("api_emergencias:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class EmergenciaCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = EmergenciaForm

    def __init__(self):
        self.service = EmergenciaService()
