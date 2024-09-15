from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import CreateController

from templates.sneat import TemplateLayout

from ..forms import DenunciaForm
from ..services import DenunciaService


class DenunciaCreateView(LoginRequiredMixin, CheckPermisosMixin, CreateView):
    permission_required = ""
    form_class = DenunciaForm
    template_name = "sneat/layout/partials/form/layout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "Asesoría jurídica"
        context["indexUrl"] = reverse_lazy("modules:index")
        context["module"] = "Asesoría jurídica"
        context["submodule"] = "Denuncias"
        context["titleForm"] = "Añadir una denuncia nueva"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("denuncias:list")
        context["urlForm"] = reverse_lazy("api_denuncias:create")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)


class DenunciaCreateApiView(CreateController, CheckPermisosMixin):
    permission_required = ""
    template_name = "sneat/layout/partials/form/layout.html"

    def __init__(self):
        self.service = DenunciaService()

    # def get_queryset(self):
    #     # self.kwargs['page']
    #     page = self.request.GET.get("page") or 1
    #     search = self.request.GET.get("search") or None

    #     return self.service.getAll(page, search)

    # def get(self, request, *args, **kwargs):
    #     if request.headers.get("x-requested-with") == "XMLHttpRequest":
    #         data = {}
    #         try:
    #             data = self.get_queryset()
    #         except Exception as e:
    #             data["error"] = str(e)
    #         return JsonResponse(data, safe=False)

    #     context = self.get_context_data(**kwargs)
    #     return render(request, self.template_name, context)
