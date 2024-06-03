from django.core.paginator import Paginator
from repositories.SocialMediaAccountRepository import SocialMediaAccountRepository
from utils.PaginatorUtil import PaginatorUtil


class SocialMediaAccountService:
    def __init__(self):
        self.repository = SocialMediaAccountRepository()

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
