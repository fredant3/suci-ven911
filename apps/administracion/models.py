from administracion.asignaciones.models import Asignacion
from administracion.averia.models import Averia, TipoAveria
from administracion.compras.model import Compra
from administracion.departamentos.models import Departamento
from administracion.inventario.models import Articulo, TipoArticulo
from administracion.sedes.models import Sede

__all__ = [
    "Departamento",
    "Articulo",
    "TipoArticulo",
    "Sede",
    "Compra",
    "Averia",
    "TipoAveria",
    "Asignacion",
]
