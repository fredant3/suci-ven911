from administracion.inventario import Articulo
from helpers.CrudMixin import CrudService
from tecnologia.repositories import TecnologiaRepository


class TecnologiaService(CrudService):
    def __init__(self):
        self.repository = TecnologiaRepository()
