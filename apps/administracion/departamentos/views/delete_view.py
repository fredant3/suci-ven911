from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from ..forms import DepartamentoForm
from ..models import Departamento
from ..services import DepartamentoService


class DepartamentoDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Departamentos"
        context["titleForm"] = "Eliminar departamento"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("departamentos:list")
        context["urlDelete"] = reverse_lazy(
            "api_departamentos:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Departamento.objects.filter(pk=id)


class DepartamentoDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = DepartamentoForm

    def __init__(self):
        self.service = DepartamentoService()
