from gestion_comunicacional.equipments.repositories.EquipmentLoanRepository import EquipmentLoanRepository


class EquipmentLoanService:
    def __init__(self):
        self.repository = EquipmentLoanRepository()

    def getAll(self):
        return self.repository.getAll()

    def getById(self, id):
        return self.repository.getById(id)
