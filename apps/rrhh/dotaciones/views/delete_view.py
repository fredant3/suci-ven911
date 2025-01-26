from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from ..forms import DotacionForm
from ..models import Dotacion
from ..services import DotacionService


class DotacionDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Dotacions"
        context["titleForm"] = "Eliminar dotacion"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("dotaciones:list")
        context["urlDelete"] = reverse_lazy(
            "api_dotaciones:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Dotacion.objects.filter(pk=id)


class DotacionDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = DotacionForm

    def __init__(self):
        self.service = DotacionService()
