from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from rrhh.educaciones.forms import EducacionForm
from rrhh.educaciones.models import Educacion
from rrhh.educaciones.services import EducacionService


class EducacionDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = "rrhh.educacion.eliminar_educacion"
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestión Humana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestión Humana"
        context["submodule"] = "Educacion"
        context["titleForm"] = "Eliminar educación"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("educaciones:list")
        context["urlDelete"] = reverse_lazy(
            "api_educaciones:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Educacion.objects.filter(pk=id)


class EducacionDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = "rrhh.educacion.eliminar_educacion"
    form_class = EducacionForm

    def __init__(self):
        self.service = EducacionService()
