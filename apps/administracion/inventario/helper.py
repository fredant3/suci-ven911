from administracion.inventario.forms import (
    ConsumibleForm,
    MobiliarioForm,
    TecnologiaForm,
    VehiculoForm,
)

tipos = {
    "tecnologia": TecnologiaForm,
    "consumible": ConsumibleForm,
    "mobiliario": MobiliarioForm,
    "vehiculo": VehiculoForm,
}


def define_type_form(kwargs):
    tipo = kwargs.get("type")
    isType = tipos.get(tipo, None)
    if isType is None:
        raise Exception("Tipo de articulo no encontrado")
    return isType
