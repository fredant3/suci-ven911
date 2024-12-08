from administracion.inventario.repositories import (
    ArticuloRepository,
    TipoArticuloRepository,
)
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

    def relationship(self, payload, *arg, **kwargs):
        payload["tipo_articulo_id"] = self.search_type_article(kwargs.get("type"))

        return payload
