from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin


class ReceptorPDFView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "presupuesto.receptor.pdf_receptor"

    def get(self, request, *args, **kwargs):
        pass
