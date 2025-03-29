from helpers.CrudMixin import CrudService
from tecnologia.usuarios.repositories import UserRepository


class UserService(CrudService):
    def __init__(self):
        self.repository = UserRepository()
