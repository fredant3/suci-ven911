from gestion_comunicacional.equipments.entities.EquipmentLoanEntity import EquipmentLoanEntity


class EquipmentLoanRepository:
    def getAll(self):
        return EquipmentLoanEntity.objects.all()

    def getById(self, id):
        return EquipmentLoanEntity.objects.get(id=id)
