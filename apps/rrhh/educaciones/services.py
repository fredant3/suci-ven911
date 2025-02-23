from helpers.CrudMixin import CrudService
from rrhh.empleados.models import Empleado  # Importar modelo Empleado
from rrhh.empleados.repositories import EmpleadoRepository
from rrhh.educaciones.repositories import EducacionRepository


class EducacionService(CrudService):
    select = (
        "id",
        "colegio",
        "codigo_titulo",
        "titulo",
        "area_conocimiento",
        "fecha_inicio",
        "fecha_culminacion",
        "enlace_certificado",
        "empleado__nombres",
    )

    def __init__(self):
        self.repository = EducacionRepository()
        self.empleado_repository = EmpleadoRepository()

    def buscar_empleado(self, empleado_id):
        return self.empleado_repository.getById(empleado_id)

    def relationship(self, payload, *arg, **kwargs):
        payload["empleado"] = self.buscar_empleado(payload.get("empleado"))
        return payload
