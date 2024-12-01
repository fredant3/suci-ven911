from administracion.inventario.forms import (
    ArticuloForm,
    ConsumibleForm,
    MobiliarioForm,
    TecnologiaForm,
    VehiculoForm,
)
from administracion.inventario.services import InventarioService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout


class ArticuloCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/layout.html"

    tipos = {
        "tecnologia": TecnologiaForm,
        "consumible": ConsumibleForm,
        "mobiliario": MobiliarioForm,
        "vehiculo": VehiculoForm,
    }

    def define_type_form(self):
        tipo = self.kwargs.get("type")
        return self.tipos.get(tipo, None)

    def get_context_data(self, **kwargs):
        self.form_class = self.define_type_form()
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administracion"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Inventario"
        context["submodule"] = "Articulo"
        context["titleForm"] = "Añadir una Articulo"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("articulos:list")
        context["urlForm"] = reverse_lazy("api_articulos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class AsignacionCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = ArticuloForm

    def __init__(self):
        self.service = InventarioService()
