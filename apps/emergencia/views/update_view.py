from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import EmergenciaForm
from ..models import Emergencia
from ..services import EmergenciaService


class EmergenciaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = EmergenciaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Emergencias"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Emergencias"
        context["submodule"] = "Emergencias"
        context["titleForm"] = "Actualizar emergancia"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("emergancias:list")
        context["urlForm"] = reverse_lazy(
            "api_emergancias:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Emergencia.objects.filter(pk=id)


class EmergenciaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = EmergenciaForm

    def __init__(self):
        self.service = EmergenciaService()
