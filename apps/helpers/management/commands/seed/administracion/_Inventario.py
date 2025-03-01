import random

import faker.providers
from administracion.inventario.models import Articulo, TipoArticulo

TIPOS_DE_ARTICULOS = [
    "tecnologia",
    "consumible",
    "mobiliario",
    "vehiculo",
]

TIPO_CONSIDCION = ["N", "U", "D"]

BIEN_NACIONAL = [
    "Computador de Escritorio",
    "Laptop",
    "Servidor",
    "Impresora",
    "Camara",
    "Televisor",
    "Amplificador",
]


class ArticuloProvider(faker.providers.BaseProvider):
    def inventario(self):
        return self.random_element(BIEN_NACIONAL)


class ArticleFake:
    def type_article():
        tiposArticulos = TipoArticulo.objects.all()

        if tiposArticulos.count() > 0:
            return None

        for tipoArticulo in TIPOS_DE_ARTICULOS:
            entity = TipoArticulo.objects.create(nombre=tipoArticulo)
            print(f"Tipo de articulo {entity.nombre} registrado")

    def article(faker):
        faker.add_provider(ArticuloProvider)
        for _ in range(15):
            tipoArticulo = TipoArticulo.objects.order_by("?").first()
            articulo = Articulo.objects.create(
                descripcion=faker.text(),
                marca=faker.name(),
                modelo=faker.name(),
                serial=random.randint(1, 18),
                placa=random.randint(1, 8),
                cantidad_combustible=random.randint(1, 18),
                codigo_bn=random.randint(1, 9),
                cantidad=random.randint(1, 18),
                tipo_articulo=tipoArticulo,
                condicion=random.choice(TIPO_CONSIDCION),
                fecha_adq=faker.date(),
                asignado=random.choice([True, False]),
            )
            print(f"Articulo {articulo.marca}, {articulo.serial} registrado")
