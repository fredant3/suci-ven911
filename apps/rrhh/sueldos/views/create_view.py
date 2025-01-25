from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from ..forms import SueldoForm
from ..services import SueldoService


class SueldoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = SueldoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Sueldos"
        context["titleForm"] = "Añadir una sueldo nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("sueldos:list")
        context["urlForm"] = reverse_lazy("api_sueldos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class SueldoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = SueldoForm

    def __init__(self):
        self.service = SueldoService()
