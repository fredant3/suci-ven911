from gestion_comunicacional.equipament.repositories.EquipamentLoanRepository import (
    EquipamentLoanRepository,
)


class EquipamentLoanService:
    def __init__(self):
        self.repository = EquipamentLoanRepository()

    def getAll(self):
        return self.repository.getAll()

    def getById(self, id):
        return self.repository.getById(id)
