from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from ..forms import SalidaForm
from ..models import Salida
from ..services import SalidaService


class SalidaDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Salidas"
        context["titleForm"] = "Eliminar salida"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("salidas:list")
        context["urlDelete"] = reverse_lazy(
            "api_salidas:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Salida.objects.filter(pk=id)


class SalidaDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = SalidaForm

    def __init__(self):
        self.service = SalidaService()
