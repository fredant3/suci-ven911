from django.core.paginator import Paginator
from gestion_comunicacional.social_activity.repositories.SocialActivityRepository import (
    SocialActivityRepository,
)
from gestion_comunicacional.utils.PaginatorUtil import PaginatorUtil


class SocialActivityService:
    def __init__(self):
        self.repository = SocialActivityRepository()

    def getAll(self, page, search=None):
        if search is None:
            entities = self.repository.getAll()
        else:
            entities = self.repository.getAllFilter(search)

        entities = self.repository.getAll()
        paginator = Paginator(entities, 15)

        return PaginatorUtil.paginate(paginator, page)

    def creator(self, post):
        return self.repository.createWithForm(post)

    def reader(self, id):
        return self.repository.getById(id)

    def updater(self, put, id):
        return self.repository.updateWithForm(id, put)

    def destroyer(self, id):
        return self.repository.delete(id)
