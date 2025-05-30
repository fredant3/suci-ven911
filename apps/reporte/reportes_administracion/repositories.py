# from administracion.averia.models import Averia
from apps.reporte.reportes_administracion.models import ReportesAdministracion
from helpers.RepositoryMixin import Repository


class ReportesAdministracionRepository(Repository):
    def __init__(self):
        self.entity = ReportesAdministracion
