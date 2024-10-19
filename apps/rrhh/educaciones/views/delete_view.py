from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import DeleteController

from templates.sneat import TemplateLayout

from ..forms import EducacionForm
from ..models import Educacion
from ..services import EducacionService


class EducacionDeleteView(LoginRequiredMixin, CheckPermisosMixin, DeleteView):
    permission_required = ""
    template_name = "sneat/layout/partials/form/delete-layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Educacions"
        context["titleForm"] = "Eliminar educacion"
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
    permission_required = ""
    form_class = EducacionForm

    def __init__(self):
        self.service = EducacionService()
