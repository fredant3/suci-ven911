from administracion.inventario.forms import ArticuloForm
from administracion.inventario.helper import define_type_form
from administracion.inventario.models import Articulo
from administracion.inventario.services import ArticuloService
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout


class TecnologiaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "tecnologia.inventario.editar_articulo"
    form_class = ArticuloForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        self.form_class = define_type_form(self.kwargs)
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tecnología"
        context["indexUrl"] = reverse_lazy("tecnologia")
        context["module"] = "Tecnología"
        context["submodule"] = "Actualizar inventario"
        context["titleForm"] = f"Actualizar articulo tipo {self.kwargs['type']}"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("tecnologia:list")
        context["urlForm"] = reverse_lazy(
            "api_articulos:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        model = Articulo.objects.filter(pk=id)
        self.kwargs["type"] = model[0].tipo_articulo.nombre
        return model


class TecnologiaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "tecnologia.inventario.editar_articulo"
    form_class = ArticuloForm

    def __init__(self):
        self.service = ArticuloService()

    def get_form_class(self):
        self.form_class = define_type_form(self.request.POST["tipo_articulo__nombre"])
        return self.form_class
