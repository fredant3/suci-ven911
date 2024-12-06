from administracion.inventario.repositories import ArticuloRepository
from django.core.exceptions import ValidationError
from django.db.models import Q
from helpers.CrudMixin import CrudService


class ArticuloService(CrudService):
    def __init__(self):
        self.repository = ArticuloRepository()

    def prepare_data(self, request, *arg, **kwargs):
        data = request.POST.copy()
        user = request.user
        if data.get("id") is None:
            data["created_by"] = user
        data["updated_by"] = user
        data["tipo_articulo"] = kwargs.get("type")
        return data
