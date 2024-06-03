from entities.SocialMediaAccountEntity import SocialMediaAccountEntity
from forms.SocialMediaAccountForm import SocialMediaAccountForm


class SocialMediaAccountRepository:
    def getAll(self):
        return SocialMediaAccountEntity.objects.all()

    def getAllFilter(self, search):
        return SocialMediaAccountEntity.objects.filter(username=search)

    def getById(self, id):
        return SocialMediaAccountEntity.objects.get(id=id)

    def create(self, data):
        entity = SocialMediaAccountEntity(**data)
        entity.save()
        return entity

    def createWithForm(self, data):
        createForm = SocialMediaAccountForm(data)

        if createForm.is_valid():
            return createForm.save()

        return createForm

    def update(self, id, data):
        entity = self.getById(id)
        for field, value in data.items():
            setattr(entity, field, value)
        entity.save()
        return entity

    def updateWithForm(self, id, data):
        entity = self.repository.getById(id)

        updateForm = SocialMediaAccountForm(data, instance=entity)

        if updateForm.is_valid():
            return updateForm.save()

        return updateForm

    def delete(self, id):
        return self.getById(id).delete()
