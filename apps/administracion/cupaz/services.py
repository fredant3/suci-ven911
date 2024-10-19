from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import CuadrantePazRepository


class CuadrantePazService(CrudService):
    def __init__(self):
        self.repository = CuadrantePazRepository()
