from administracion.inventario.forms import ArticuloForm
from administracion.inventario.services import InventarioService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout


class ArticuloCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = ArticuloForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administracion"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Inventario"
        context["submodule"] = "Articulo"
        context["titleForm"] = "Añadir una Articulo"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("Articulo:list")
        context["urlForm"] = reverse_lazy("api_Articulo:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class AsignacionCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = ArticuloForm

    def __init__(self):
        self.service = InventarioService()
