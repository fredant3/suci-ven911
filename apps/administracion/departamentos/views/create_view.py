from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from ..forms import DepartamentoForm
from ..services import DepartamentoService


class DepartamentoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = DepartamentoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Departamentos"
        context["titleForm"] = "Añadir una departamento nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("departamentos:list")
        context["urlForm"] = reverse_lazy("api_departamentos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class DepartamentoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = DepartamentoForm

    def __init__(self):
        self.service = DepartamentoService()
