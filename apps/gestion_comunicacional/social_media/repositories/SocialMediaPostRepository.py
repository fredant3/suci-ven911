from entities.SocialMediaPostEntity import SocialMediaPostEntity
from index.mixins.RepositoryMixin import Repository


class SocialMediaPostRepository(Repository):
    def __init__(self):
        self.entity = SocialMediaPostEntity
