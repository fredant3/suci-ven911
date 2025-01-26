from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController

from templates.sneat import TemplateLayout

from ..forms import DenunciaForm
from ..models import Denuncia
from ..services import DenunciaService


class DenunciaUpdateView(LoginRequiredMixin, CheckPermisosMixin, UpdateView):
    permission_required = ""
    form_class = DenunciaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Denuncias"
        context["titleForm"] = "Actualizar denuncia"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("denuncias:list")
        context["urlForm"] = reverse_lazy(
            "api_denuncias:update", args=[self.kwargs.get("pk")]
        )
        context["methodForm"] = "PUT"
        return TemplateLayout.init(self, context)

    def get_queryset(self):
        id = self.kwargs.get("pk")
        return Denuncia.objects.filter(pk=id)


class DenunciaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = DenunciaForm

    def __init__(self):
        self.service = DenunciaService()
