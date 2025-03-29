from gestion_comunicacional.equipments.entities.EquipmentEntity import EquipmentEntity
from helpers.RepositoryMixin import Repository


class EquipmentRepository(Repository):
    def __init__(self):
        self.entity = EquipmentEntity
