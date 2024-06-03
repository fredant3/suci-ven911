from gestion_comunicacional.equipament.entities.EquipamentLoanEntity import (
    EquipamentLoanEntity,
)


class EquipamentLoanRepository:
    def getAll(self):
        return EquipamentLoanEntity.objects.all()

    def getById(self, id):
        return EquipamentLoanEntity.objects.get(id=id)
