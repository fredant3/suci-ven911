from administracion.asignaciones.repositories import AsignacionRepository
from django.db.models import Q
from helpers.CrudMixin import CrudService


class AsignacionService(CrudService):
    def __init__(self):
        self.repository = AsignacionRepository()
