from administracion.compras.repositories import CompraRepository
from helpers.CrudMixin import CrudService
from administracion.inventario.repositories import ArticuloRepository


class CompraService(CrudService):
    select = (
        "id",
        "articulo__descripcion",
        "n_orden",
        "valor_bs",
    )

    def __init__(self):
        self.repository = CompraRepository()
        self.articulo_repository = ArticuloRepository()

    def buscar_articulo(self, articulo_id):
        return self.articulo_repository.getById(articulo_id)

    def relationship(self, payload, *arg, **kwargs):
        payload["articulo"] = self.buscar_articulo(payload.get("articulo"))
        return payload
