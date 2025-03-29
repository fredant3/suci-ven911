from gestion_comunicacional.social_media.repositories.SocialMediaAccountRepository import SocialMediaAccountRepository
from index.mixins.CrudMixin import CrudService


class SocialMediaAccountService(CrudService):
    def __init__(self):
        self.repository = SocialMediaAccountRepository()
