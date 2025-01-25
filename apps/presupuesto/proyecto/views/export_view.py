from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin


class ProyectoPDFView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = ""

    def get(self, request, *args, **kwargs):
        pass
