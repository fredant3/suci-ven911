from helpers.CrudMixin import CrudService
from rrhh.empleados.models import Empleado  # Importar modelo Empleado
from rrhh.empleados.repositories import EmpleadoRepository
from rrhh.educaciones.repositories import EducacionRepository


class EducacionService(CrudService):
    select = (
        "id",
        "banco",
        "tipo",
        "numero_cuenta",
        "pago_movil",
        "telefono",
        "empleado__nombres",
    )

    def __init__(self):
        self.repository = EducacionRepository()
