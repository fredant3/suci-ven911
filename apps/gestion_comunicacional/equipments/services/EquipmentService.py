from gestion_comunicacional.equipments.repositories.EquipmentRepository import EquipmentRepository
from helpers.CrudMixin import CrudService


class EquipmentService(CrudService):
    def __init__(self):
        self.repository = EquipmentRepository()
