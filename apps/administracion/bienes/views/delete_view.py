from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from ..forms import BienForm
from ..models import Bien
from ..services import BienService


class BienDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Bienes"
        context["titleForm"] = "Eliminar bien"
        context["tag"] = "Eliminar"
        context["listUrl"] = reverse_lazy("bienes:list")
        context["urlDelete"] = reverse_lazy(
            "api_bienes:delete", args=[self.kwargs.get("pk")]
        )
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Bien.objects.filter(pk=id)


class BienDeleteApiView(DeleteController, CheckPermisosMixin):
    permission_required = ""
    form_class = BienForm

    def __init__(self):
        self.service = BienService()
