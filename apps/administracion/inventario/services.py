from administracion.inventario.repositories import InventarioRepository
from django.core.exceptions import ValidationError
from django.db.models import Q
from helpers.CrudMixin import CrudService


class InventarioService(CrudService):
    def __init__(self):
        self.repository = InventarioRepository()

    def prepare_data(self, request):
        data = request.POST.copy()
        user = request.user
        if data.get("id") is None:
            data["created_by"] = user
        data["updated_by"] = user
        data["tipo_articulo"] = "tecnologia"
        print(data)
        return data
