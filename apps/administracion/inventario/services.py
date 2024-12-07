from administracion.inventario.repositories import (
    ArticuloRepository,
    TipoArticuloRepository,
)
from django.core.exceptions import ValidationError
from django.db.models import Q
from helpers.CrudMixin import CrudService


class ArticuloService(CrudService):
    def __init__(self):
        self.repository = ArticuloRepository()
        self.repositoryTypeArticle = TipoArticuloRepository()

    def search_type_article(self, tipo_articulo):
        search = self.repositoryTypeArticle.getFilter(
            ("nombre", tipo_articulo), ("id",)
        ).first()

        return search["id"] if search is not None else None

    def prepare_data(self, request, *arg, **kwargs):
        data = request.POST.copy()
        data["tipo_articulo_id"] = self.search_type_article(kwargs.get("type"))

        user = request.user
        if data.get("id") is None:
            data["created_by"] = user.username
        data["updated_by"] = user.username

        return data
