import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from templates.sneat import TemplateLayout


class OrganizacionView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""
    url_redirect = reverse_lazy("modules:index")
    template_name = "dashborad/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organizaciones"
        context["module"] = "Organizacion"
        context["listApiUrl"] = reverse_lazy("api_organizacion")
        context["cards"] = self.getCards()
        return TemplateLayout.init(self, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Organización"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Organización"
        context["submodule"] = "Dashboard Organización"
        context["submoduleList"] = (
            ("Normativas", reverse_lazy("normativas:list")),
            ("Reglamentos", reverse_lazy("reglamentos:list")),
        )
        return TemplateLayout.init(self, context)
