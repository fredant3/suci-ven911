from helpers.CrudMixin import CrudService

from rrhh.cargos.repositories import CargoRepository


class CargoService(CrudService):
    def __init__(self):
        self.repository = CargoRepository()
