from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import BienRepository


class BienService(CrudService):
    def __init__(self):
        self.repository = BienRepository()
