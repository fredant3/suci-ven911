from helpers.CrudMixin import CrudService

from .repositories import InfraestructuraRepository


class InfraestructuraService(CrudService):
    def __init__(self):
        self.repository = InfraestructuraRepository()
