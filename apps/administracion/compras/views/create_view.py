from administracion.compras.forms import CompraForm
from administracion.compras.services import CompraService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout


class CompraCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = CompraForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administracion"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asignaciones"
        context["submodule"] = "compra"
        context["titleForm"] = "Añadir una compra"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("compra:list")
        context["urlForm"] = reverse_lazy("api_compra:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class ComprasCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = CompraForm

    def __init__(self):
        self.service = CompraService()
