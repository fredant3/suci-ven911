from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from templates.sneat import TemplateLayout


class EmergenciaView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "emergencia_index"
    url_redirect = reverse_lazy("modules:index")
    template_name = "dashborad/index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Operaciones"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Operaciones"
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
            ("Operaciones", reverse_lazy("operaciones:list")),
            ("Incidencias", reverse_lazy("operaciones_incidencias:list")),
            ("Organismos", reverse_lazy("organismo:list")),
        )
        return TemplateLayout.init(self, context)
