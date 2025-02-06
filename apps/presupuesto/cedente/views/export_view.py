from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin


class CedentePDFView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "presupuesto.cedente.pdf_cedente"

    def get(self, request, *args, **kwargs):
        pass
