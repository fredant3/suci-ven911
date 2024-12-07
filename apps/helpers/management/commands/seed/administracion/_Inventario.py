from administracion.inventario.models import Articulo, TipoArticulo

TIPOS_DE_ARTICULOS = [
    "tecnologia",
    "consumible",
    "mobiliario",
    "vehiculo",
]

TIPO_CONSIDCION = ["N", "U", "D"]


class ArticleFake:
    def type_article():
        tiposArticulos = TipoArticulo.objects.all()

        if tiposArticulos.count() > 0:
            return None

        for tipoArticulo in TIPOS_DE_ARTICULOS:
            entity = TipoArticulo.objects.create(nombre=tipoArticulo)
            print(f"Tipo de articulo {entity.nombre} registrado")

    def article():
        pass
