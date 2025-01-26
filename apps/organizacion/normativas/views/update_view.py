from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from helpers.CheckPermisosMixin import CheckPermisosMixin
from helpers.ControllerMixin import UpdateController
from organizacion.normativas.forms import NormativaForm
from organizacion.normativas.models import Normativa
from organizacion.normativas.services import NormativaService
from templates.sneat import TemplateLayout

class NormativaUpdateView(LoginRequiredMixin, CheckPermisosMixin, View):
    permission_required = ""
    form_class = NormativaForm
    template_name = "sneat/layout/partials/form/layout_normativas_editar.html"
    success_url = reverse_lazy("normativas:list")

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("pk")
        normativa = get_object_or_404(Normativa, pk=id)
        form = self.form_class(instance=normativa)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get("pk")
        normativa = get_object_or_404(Normativa, pk=id)
        form = self.form_class(request.POST, request.FILES, instance=normativa)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "success"}, status=200)
        return JsonResponse({"message": "error", "errors": form.errors}, status=400)

    def get_context_data(self, **kwargs):
        id = self.kwargs.get("pk")
        data = Normativa.objects.filter(pk=id).all
        context = kwargs
        context["titlePage"] = "Organizacion"
        context["indexUrl"] = reverse_lazy("organizacion")
        context["module"] = "Organizacion"
        context["submodule"] = "Normativas"
        context["titleForm"] = "Actualizar normativa"
        context["tag"] = "Editar"
        context["listUrl"] = reverse_lazy("normativas:list")
        context["urlForm"] = reverse_lazy("api_normativas:update", args=[self.kwargs.get("pk")])
        context["methodForm"] = "POST"
        context["formu"] = data
        return TemplateLayout.init(self, context)

class NormativaUpdateApiView(UpdateController, CheckPermisosMixin):
    permission_required = ""
    form_class = NormativaForm

    def __init__(self):
        self.service = NormativaService()

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get("pk")
        normativa = get_object_or_404(Normativa, pk=id)
        form = self.form_class(request.POST, request.FILES, instance=normativa)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Se ha registrado con éxito."})
        else:
            return JsonResponse({"message": "error", "errors": form.errors}, status=400)
