from gestion_comunicacional.equipments.entities.EquipmentEntity import EquipmentEntity
from index.mixins.RepositoryMixin import Repository


class EquipmentRepository(Repository):
    def __init__(self):
        self.entity = EquipmentEntity
