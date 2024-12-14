from administracion.inventario.forms import ArticuloForm
from administracion.inventario.helper import define_type_form
from administracion.inventario.services import ArticuloService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout


class ArticuloCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/layout.html"
    form_class = ArticuloForm

    def get_context_data(self, **kwargs):
        self.form_class = define_type_form(self.kwargs)
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Administracion"
        context["indexUrl"] = reverse_lazy("administracion")
        context["module"] = "Administracion"
        context["submodule"] = "Articulo"
        context["titleForm"] = f"Añadir articulo tipo {self.kwargs.get("type")}"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("articulos:list")
        context["urlForm"] = reverse_lazy(
            "api_articulos:create", args=[self.kwargs.get("type")]
        )
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class ArtiluloCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    form_class = ArticuloForm

    def __init__(self):
        self.service = ArticuloService()

    def get_form_class(self):
        self.form_class = define_type_form(self.kwargs)
        return self.form_class
