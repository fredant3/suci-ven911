from rrhh.tipos_sueldos.models import TipoSueldo
import random

TIPOS_DE_SUELDOS = [
    "ticket",
    "guerra",
    "discapacidad",
    "menor_12",
    "hijos_13_18",
    "hijos_discapacidad",
    "profesionalismo",
    "minimo",
]


class TipoSueldoFake:
    def tipos_sueldos(faker):
        # for tipo_sueldo in TIPOS_DE_SUELDOS:
        #     model = TipoSueldo.objects.create(
        #         tipo=tipo_sueldo,
        #         monto=faker.pricetag(),
        #         descripcion=faker.texts(nb_texts=2),
        #         estatus=random.choice(["act", "sup"]),
        #     )
        #     print(f"Tipo de sueldo {model.tipo} registrado")
