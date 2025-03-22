from helpers.RepositoryMixin import Repository
from users.auth.models import User


class UserRepository(Repository):
    def __init__(self):
        self.entity = User
