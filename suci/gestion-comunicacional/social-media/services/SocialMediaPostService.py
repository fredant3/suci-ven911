from repositories.SocialMediaPostRepository import SocialMediaPostRepository


class SocialMediaPostService:
    def __init__(self):
        self.repository = SocialMediaPostRepository()

    def getAll(self):
        return self.repository.getAll()

    def getById(self, id):
        return self.repository.getById(id)
