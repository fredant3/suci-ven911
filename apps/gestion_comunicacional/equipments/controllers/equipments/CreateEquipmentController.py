from gestion_comunicacional.equipments.forms.EquipmentForm import EquipmentForm
from gestion_comunicacional.equipments.services.EquipmentService import EquipmentService
from index.mixins.ControllerMixin import CreateController
from templates.sneat import TemplateLayout

from django.urls import reverse_lazy


class CreateEquipment(CreateController):
    template_name = "gc/equipments/equipments/create.html"
    form_class = EquipmentForm

    def __init__(self):
        self.service = EquipmentService()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titlePage"] = "gc_eq_equipments_title_page"
        context["indexUrl"] = reverse_lazy("gc:info")
        context["module"] = "gc_module_name"
        context["submodule"] = "gc_eq_module_name"
        context["titleForm"] = "gc_eq_equipments_title_form"
        context["tag"] = "Registrar"
        context["listUrl"] = reverse_lazy("gc:eq:listing-equipments")
        context["urlForm"] = reverse_lazy("gc:eq:create-equipments")
        context["methodForm"] = "POST"
        return TemplateLayout.init(self, context)
