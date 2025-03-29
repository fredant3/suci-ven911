from gestion_comunicacional.equipments.repositories.EquipmentRepository import EquipmentRepository
from index.mixins.CrudMixin import CrudService


class EquipmentService(CrudService):
    def __init__(self):
        self.repository = EquipmentRepository()
