from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin

from templates.sneat import TemplateLayout

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from asesoria.denuncias.models import Denuncia


class AsesoriaView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ("asesoria.ver_denuncia", "asesoria.ver_registro_filmico")
    url_redirect = reverse_lazy("modules:index")
    template_name = "dashborad/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría"
        context["submodule"] = "Inicio Asesoría"
        context["submoduleList"] = (
            ("Denuncias", reverse_lazy("denuncias:list")),
            ("Fílmicos", reverse_lazy("filmicos:list")),
        )

        content_type = ContentType.objects.get_for_model(Denuncia)
        permissions = Permission.objects.filter(content_type=content_type)
        for perm in permissions:
            print(perm.name, perm.codename)

        return TemplateLayout.init(self, context)
