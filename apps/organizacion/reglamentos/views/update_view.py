from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController
from organizacion.reglamentos.forms import ReglamentoForm
from organizacion.reglamentos.models import Reglamento
from organizacion.reglamentos.services import ReglamentoService
from templates.sneat import TemplateLayout

class ReglamentoUpdateView(LoginRequiredMixin, CheckPermisosMixin, View):
    permission_required = ""
    form_class = ReglamentoForm
    template_name = "sneat/layout/partials/form/layout_reglamentos_editar.html"
    success_url = reverse_lazy("reglamentos:list")

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("pk")
        reglamento = get_object_or_404(Reglamento, pk=id)
        form = self.form_class(instance=reglamento)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get("pk")
        reglamento = get_object_or_404(Reglamento, pk=id)
        form = self.form_class(request.POST, request.FILES, instance=reglamento)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "success"}, status=200)
        return JsonResponse({"message": "error", "errors": form.errors}, status=400)

    def get_context_data(self, **kwargs):
        id = self.kwargs.get("pk")
        data = Reglamento.objects.filter(pk=id).all
        context = kwargs
        context["titlePage"] = "Organizacion"
        context["indexUrl"] = reverse_lazy("organizacion")
        context["module"] = "Organizacion"
        context["submodule"] = "Reglamentos"
        context["titleForm"] = "Actualizar reglamento"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("reglamentos:list")
        context["urlForm"] = reverse_lazy("api_reglamentos:update", args=[self.kwargs.get("pk")])
        context["methodForm"] = "POST"
        context["formu"] = data
        return TemplateLayout.init(self, context)

class ReglamentoUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = ReglamentoForm

    def __init__(self):
        self.service = ReglamentoService()

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get("pk")
        reglamento = get_object_or_404(Reglamento, pk=id)
        form = self.form_class(request.POST, request.FILES, instance=reglamento)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Se ha registrado con éxito."})
        else:
            return JsonResponse({"message": "error", "errors": form.errors}, status=400)
