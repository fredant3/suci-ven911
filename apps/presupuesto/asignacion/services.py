from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import AsignacionRepository


class AsignacionService(CrudService):
    def __init__(self):
        self.repository = AsignacionRepository()
