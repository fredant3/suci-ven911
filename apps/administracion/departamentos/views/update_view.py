from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import DepartamentoForm
from ..models import Departamento
from ..services import DepartamentoService


class DepartamentoUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = DepartamentoForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Departamentos"
        context["titleForm"] = "Actualizar departamento"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("departamentos:list")
        context["urlForm"] = reverse_lazy(
            "api_departamentos:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Departamento.objects.filter(pk=id)


class DepartamentoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = DepartamentoForm

    def __init__(self):
        self.service = DepartamentoService()
