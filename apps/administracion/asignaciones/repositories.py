from administracion.asignaciones.models import Asignacion
from helpers.RepositoryMixin import Repository


class AsignacionRepository(Repository):
    def __init__(self):
        self.entity = Asignacion

    def getAll(self, select, orderBy, orderAsc):
        orderBy = orderBy if orderBy else "id"
        order = orderBy if orderAsc == "asc" else "-" + orderBy
        return (
            self.entity.objects.all()
            .order_by(order)
            .values(
                "id",
                "articulo__serial",
                "sede__sede",
                "departamento__nombre",
                "cantidad",
                "descripcion",
                "observaciones",
                "created_by",
            )
        )

    def getFilter(self, criteria, select="", orderBy="id", orderAsc="-"):
        orderBy = orderBy if orderBy else "id"
        order = orderBy if orderAsc == "asc" else "-" + orderBy

        return self.entity.objects.filter(criteria).order_by(order).values(*select)
