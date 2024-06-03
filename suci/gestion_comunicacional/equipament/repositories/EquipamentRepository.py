from gestion_comunicacional.equipament.entities.EquipamentEntity import EquipamentEntity
from gestion_comunicacional.equipament.forms.EquipamentForm import EquipamentForm


class EquipamentRepository:
    def getAll(self):
        return EquipamentEntity.objects.all()

    def getAllFilter(self, search):
        return EquipamentEntity.objects.filter(username=search)

    def getById(self, id):
        return EquipamentEntity.objects.get(id=id)

    def create(self, data):
        entity = EquipamentEntity(**data)
        entity.save()
        return entity

    def createWithForm(self, data):
        createForm = EquipamentForm(data)

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

        updateForm = EquipamentForm(data, instance=entity)

        if updateForm.is_valid():
            return updateForm.save()

        return updateForm

    def delete(self, id):
        return self.getById(id).delete()
