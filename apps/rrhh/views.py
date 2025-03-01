from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from templates.sneat import TemplateLayout


class GestionHumanaView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "gestion_humana_index"
    url_redirect = reverse_lazy("modules:index")
    template_name = "widzard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestion Humana"
        context["indexUrl"] = reverse_lazy("gestion_humana")
        context["module"] = "Gestion Humana"
        context["submodule"] = "Cargos"
        context["titleForm"] = "Añadir una cargo nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("cargos:list")
        context["urlForm"] = reverse_lazy("api_cargos:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)

        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestion Humana"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Gestion Humana"
        context["submodule"] = "Dashboard Gestion Humana"

        return TemplateLayout.init(self, context)
