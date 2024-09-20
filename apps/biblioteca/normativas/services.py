from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import DenunciaRepository


class DenunciaService(CrudService):
    def __init__(self):
        self.repository = DenunciaRepository()
