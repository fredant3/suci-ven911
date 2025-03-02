from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from rrhh.educaciones.forms import EducacionForm
from rrhh.educaciones.models import Educacion
from rrhh.educaciones.services import EducacionService


class EducacionUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = "rrhh.educacion.editar_educacion"
    form_class = EducacionForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Huamana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Huamana"
        context["submodule"] = "Educaciones"
        context["titleForm"] = "Actualizar educación"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("educaciones:list")
        context["urlForm"] = reverse_lazy(
            "api_educaciones:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Educacion.objects.filter(pk=id)


class EducacionUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = "rrhh.educacion.editar_educacion"
    form_class = EducacionForm

    def __init__(self):
        self.service = EducacionService()
