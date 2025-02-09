from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin


class AccionPDFView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "presupuesto.acciones.pdf_accion"

    def get(self, request, *args, **kwargs):
        pass
