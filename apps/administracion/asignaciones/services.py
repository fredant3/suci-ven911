from administracion.asignaciones.repositories import AsignacionRepository
from administracion.departamentos.repositories import DepartamentoRepository
from administracion.inventario.repositories import ArticuloRepository
from administracion.sedes.repositories import SedeRepository
from django.db.models import Q
from helpers.CrudMixin import CrudService


class AsignacionService(CrudService):
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

    def prepare_data(self, request, *arg, **kwargs):
        data = request.POST.copy()
        data["articulo"] = self.search_article(data.get("articulo"))
        data["sede"] = self.search_sede(data.get("sede"))
        data["departamento"] = self.search_departamento(data.get("departamento"))

        user = request.user
        if data.get("id") is None:
            data["created_by"] = user.username
        data["updated_by"] = user.username

        return data
