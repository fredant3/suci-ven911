from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from templates.sneat import TemplateLayout


class tecnologiaView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "tecnologia_index"
    url_redirect = reverse_lazy("modules:index")
    template_name = "dashborad/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Tecnologia"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Tecnologia"
        context["submodule"] = "Tecnologia"
        context["submoduleList"] = (
            ("Inventario", reverse_lazy("tecnologia:list")),
            ("Averia", reverse_lazy("averias:list")),
            ("Grupos", reverse_lazy("grupos:list")),
            ("Usuarios", reverse_lazy("user:list")),
            ("Auditoria", reverse_lazy("user:list")),
        )
        return TemplateLayout.init(self, context)
