from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from emergencia.forms import EmergenciaForm
from emergencia.models import Emergencia
from emergencia.services import EmergenciaService
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout


class EmergenciaDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Emergencias"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Emergencias"
        context["submodule"] = "Emergencias"
        context["titleForm"] = "Eliminar emergencia"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("emergencias:list")
        context["urlDelete"] = reverse_lazy(
            "api_emergencias:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Emergencia.objects.filter(pk=id)


class EmergenciaDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = EmergenciaForm

    def __init__(self):
        self.service = EmergenciaService()
