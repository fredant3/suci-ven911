from gestion_comunicacional.social_media.repositories.SocialMediaPostRepository import SocialMediaPostRepository
from index.mixins.CrudMixin import CrudService


class SocialMediaPostService(CrudService):
    def __init__(self):
        self.repository = SocialMediaPostRepository()
