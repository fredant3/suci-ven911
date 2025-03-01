from helpers.CrudMixin import CrudService

from presupuesto.proyecto.repositories import ProyectoRepository


class ProyectoService(CrudService):
    def __init__(self):
        self.repository = ProyectoRepository()
