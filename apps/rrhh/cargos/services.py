from django.db.models import Q
from helpers.CrudMixin import CrudService

from .repositories import CargoRepository


class CargoService(CrudService):
    def __init__(self):
        self.repository = CargoRepository()
