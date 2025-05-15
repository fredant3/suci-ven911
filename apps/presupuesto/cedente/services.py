import datetime
from helpers.CrudMixin import CrudService
from presupuesto.cedente.repositories import CedenteRepository
from presupuesto.receptor.models import Receptor
from django.db.models import Q


class CedenteService(CrudService):
    def __init__(self):
        self.repository = CedenteRepository()

    def criteria(self, search, arg=None):
        query = Q()
        if search:
            query &= Q(idc__icontains=search) | Q(espefc__icontains=search)
        return query

    def destroyer(self, payload):
        deleted_at = {
            "deleted_by": payload.deleted_by,
            "updated_by": payload.updated_by,
            "deleted_at": datetime.datetime.now(),
            "updated_at": datetime.datetime.now(),
        }
        Receptor.objects.filter(cedente=payload).update(**deleted_at)
        return self.repository.delete(payload)
