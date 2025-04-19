from helpers.CrudMixin import CrudService
from potencia.uri.repositories import UriRepository


class UriService(CrudService):

    select = {
        "id",
        "fecha_atencion",
        "nombrepaciente",
        "apellidopaciente",
        "estado",
    }

    def __init__(self):
        self.repository = UriRepository()
