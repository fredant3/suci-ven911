from administracion.asignaciones.repositories import AsignacionRepository
from administracion.departamentos.repositories import DepartamentoRepository
from administracion.inventario.repositories import ArticuloRepository
from administracion.sedes.repositories import SedeRepository
from helpers.CrudMixin import CrudService


class AsignacionService(CrudService):
    select = (
        "id",
        "articulo__serial",
        "sede__sede",
        "departamento__nombre",
        "cantidad",
        "descripcion",
        "observaciones",
        "created_by",
    )

    def __init__(self):
        self.repository = AsignacionRepository()
        self.repositoryArticle = ArticuloRepository()
        self.repositorySede = SedeRepository()
        self.repositoryDepartamento = DepartamentoRepository()

    def search_article(self, articuloId):
        return self.repositoryArticle.getById(articuloId)

    def search_sede(self, sedeId):
        return self.repositorySede.getById(sedeId)

    def search_departamento(self, departamentoId):
        return self.repositoryDepartamento.getById(departamentoId)

    def relationship(self, payload, *arg, **kwargs):
        payload["articulo"] = self.search_article(payload.get("articulo"))
        payload["sede"] = self.search_sede(payload.get("sede"))
        payload["departamento"] = self.search_departamento(payload.get("departamento"))

        return payload
