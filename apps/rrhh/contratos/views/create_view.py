from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from ..forms import ContratoForm
from ..services import ContratoService


class ContratoCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = ContratoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Contratos"
        context["titleForm"] = "Añadir una contrato nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("contratos:list")
        context["urlForm"] = reverse_lazy("api_contratos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class ContratoCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = ContratoForm

    def __init__(self):
        self.service = ContratoService()
