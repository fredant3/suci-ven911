from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import FamiliarRepository


class FamiliarService(CrudService):
    def __init__(self):
        self.repository = FamiliarRepository()
