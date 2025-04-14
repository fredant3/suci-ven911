from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from templates.sneat import TemplateLayout
from django.urls import reverse_lazy
from helpers.CheckPermisosMixin import CheckPermisosMixin


class InfoController(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "gestioncomunicacional_index"
    url_redirect = reverse_lazy("modules:index")
    template_name = "dashborad/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Gestion Comunicacional"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Gestion Comunicacional"
        context["submodule"] = "Gestion Comunicacional"
        context["data"] = [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380]
        context["labels"] = [
            "South Korea",
            "Canada",
            "United Kingdom",
            "Netherlands",
            "Italy",
            "France",
            "Japan",
            "United States",
            "China",
            "Germany",
        ]
        context["submoduleList"] = (
            ("Gestion Comunicacional", reverse_lazy("gestioncomunicacional:list")),
            # ("Averia", reverse_lazy("averias:list")),
        )
        return TemplateLayout.init(self, context)
