from gestion_comunicacional.social_media.entities.SocialMediaAccountEntity import SocialMediaAccountEntity
from index.mixins.RepositoryMixin import Repository


class SocialMediaAccountRepository(Repository):
    def __init__(self):
        self.entity = SocialMediaAccountEntity
