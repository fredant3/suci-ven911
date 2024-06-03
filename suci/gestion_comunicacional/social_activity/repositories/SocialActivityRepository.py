from gestion_comunicacional.social_activity.entities.SocialActivityEntity import (
    SocialActivityEntity,
)
from gestion_comunicacional.social_activity.forms.SocialActivityForm import (
    SocialActivityForm,
)


class SocialActivityRepository:
    def getAll(self):
        return SocialActivityEntity.objects.all()

    def getAllFilter(self, search):
        return SocialActivityEntity.objects.filter(username=search)

    def getById(self, id):
        return SocialActivityEntity.objects.get(id=id)

    def create(self, data):
        entity = SocialActivityEntity(**data)
        entity.save()
        return entity

    def createWithForm(self, data):
        createForm = SocialActivityForm(data)

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

        updateForm = SocialActivityForm(data, instance=entity)

        if updateForm.is_valid():
            return updateForm.save()

        return updateForm

    def delete(self, id):
        return self.getById(id).delete()
