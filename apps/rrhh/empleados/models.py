from django.db.models import (
    DateField,
    EmailField,
    CharField,
    BooleanField,
    IntegerField,
)
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel
from helpers.models import (
    ESTADO_CIVIL_CHOICES,
    SEXO_CHOICES,
    NACIONALIDAD_CHOICES,
    TIPO_SANGRE_CHOICES,
    TIPO_CONTRATOS,
)
from helpers.validForm import (
    PositiveIntegerValidator,
    TextValidator,
    UnicodeAlphaSpaceValidator,
    PhoneNumberValidator,
)
from django.core.validators import (
    MinValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
)

ESTATUS_CHOICES = (
    ("act", "Activo"),
    ("vac", "En vacaciones"),
    ("sus", "Suspendido"),
    ("des", "Se despedio"),
    ("ren", "Ha renunciado"),
)


class Empleado(BaseModel):
    estatus = CharField(max_length=3, choices=ESTATUS_CHOICES)
    nombres = CharField(
        "Nombres del empleado",
        max_length=90,
        validators=[
            MinLengthValidator(9),
            MaxLengthValidator(90),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    apellidos = CharField(
        "Apellidos del empleado",
        max_length=90,
        validators=[
            MinLengthValidator(9),
            MaxLengthValidator(90),
            UnicodeAlphaSpaceValidator(),
        ],
    )
    nacionalidad = CharField("Nacionalidad", max_length=2, choices=NACIONALIDAD_CHOICES)
    cedula = CharField("Cedula de identidad", max_length=15, unique=True)
    sexo = CharField("Genero", max_length=1, choices=SEXO_CHOICES)
    fecha_nacimiento = DateField("Fecha de nacimiento")
    estado_civil = CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES)
    tipo_sangre = CharField(max_length=3, choices=TIPO_SANGRE_CHOICES)
    email = EmailField(blank=True, null=True)
    telefono = CharField(
        "Telefono del empleado",
        max_length=20,
        validators=[
            MinLengthValidator(11),
            MaxLengthValidator(20),
            PhoneNumberValidator(),
        ],
    )
    direccion = CharField(
        max_length=180,
        validators=[
            MinLengthValidator(9),
            MaxLengthValidator(180),
            TextValidator(),
        ],
    )
    estudia = BooleanField(default=False)
    discapacitado = BooleanField(default=False)
    contratos = CharField(max_length=3, choices=TIPO_CONTRATOS)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = "empleado"
        verbose_name_plural = "empleados"
        permissions = [
            ("listar_empleado", "Puede listar empleados"),
            ("agregar_empleado", "Puede agregar empleado"),
            ("ver_empleado", "Puede ver empleado"),
            ("editar_empleado", "Puede actualizar empleado"),
            ("eliminar_empleado", "Puede eliminar empleado"),
            ("exel_empleado", "Puede exportar empleado a excel"),
        ]
