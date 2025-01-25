from helpers.CrudMixin import CrudService

from .repositories import SedeRepository


class SedeService(CrudService):
    def __init__(self):
        self.repository = SedeRepository()
