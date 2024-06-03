from entities.SocialMediaPostEntity import SocialMediaPostEntity


class SocialMediaPostRepository:
    def getAll(self):
        return SocialMediaPostEntity.objects.all()

    def getById(self, id):
        return SocialMediaPostEntity.objects.get(id=id)
