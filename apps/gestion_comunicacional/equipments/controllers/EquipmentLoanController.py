from gestion_comunicacional.equipments.services.EquipmentLoanService import EquipmentLoanService

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


class ListEquipmentLoan(LoginRequiredMixin, ListView):
    template_name = "gc/equipments.html"

    def __init__(self):
        self.service = EquipmentLoanService()

    def get(self, request):
        page = request.GET.get("page") or 1
        search = None

        if "search" in request.GET:
            search = request.GET["search"]

        entities = self.service.getAll(page, search)

        return render(request, self.template_name, {"entities": entities})


class CreateEquipmentLoan(LoginRequiredMixin, CreateView):
    template_name = "gc/equipments.html"

    def __init__(self):
        self.service = EquipmentLoanService()

    def post(self, request):
        entity = self.service.creator(request.POST)

        return render(request, self.template_name, {"entity": entity})


class ReadEquipmentLoan(LoginRequiredMixin, DetailView):
    template_name = "gc/equipments.html"

    def __init__(self):
        self.service = EquipmentLoanService()

    def get(self, request, pk):
        entity = self.service.getById(pk)

        if not entity:
            return HttpResponse(status=404)

        return render(request, self.template_name, {"entity": entity})


class UpdateEquipmentLoan(LoginRequiredMixin, UpdateView):
    template_name = "gc/equipments.html"

    def __init__(self):
        self.service = EquipmentLoanService()

    def post(self, request, pk):
        entity = self.service.updater(request.PUT, pk)

        return render(request, self.template_name, {"entity": entity})


class DeleteEquipmentLoan(LoginRequiredMixin, DeleteView):
    template_name = "gc/equipments.html"

    def __init__(self):
        self.service = EquipmentLoanService()

    def post(self, request, pk):
        entity = self.service.destroyer(pk)

        return render(request, self.template_name, {"entity": entity})
