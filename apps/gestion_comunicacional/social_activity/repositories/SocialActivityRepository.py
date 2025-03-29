from gestion_comunicacional.social_activity.entities.SocialActivityEntity import SocialActivityEntity
from index.mixins.RepositoryMixin import Repository


class SocialActivityRepository(Repository):
    def __init__(self):
        self.entity = SocialActivityEntity
