from asesoria.denuncias.models import Denuncia
from django.forms import (
    TextInput,
    CharField,
    EmailField,
    DateInput,
    EmailInput,
)
from helpers.FormBase import FormBase
from helpers.validForm import validate_cedula, validate_email, CedulaVenezolanaValidator


class DenunciaForm(FormBase):
    nombres_denunciante = CharField(
        widget=TextInput(attrs={"placeholder": "Ingrese el nombre del denunciante"}),
    )
    apellidos_denunciante = CharField(
        widget=TextInput(attrs={"placeholder": "Ingrese el apellido del denunciante"}),
    )
    cedula_denunciante = CharField(
        widget=TextInput(attrs={"placeholder": "Ingrese la cédula del denunciante"}),
        validators=[CedulaVenezolanaValidator()],
    )
    telefono_denunciante = CharField(
        label="Teléfono del denunciante",
        widget=TextInput(attrs={"placeholder": "Ingrese el teléfono del denunciante"}),
    )
    email_denunciante = EmailField(
        max_length=60,
        required=False,
        label="Correo electrónico del denunciante",
        widget=EmailInput(
            attrs={"placeholder": "Ingrese el correo electrónico del denunciante"}
        ),
        validators=[validate_email],
    )
    direccion_denunciante = CharField(
        label="Dirección del denunciante",
        widget=TextInput(attrs={"placeholder": "Ingrese la dirección del denunciante"}),
    )

    nombres_denunciado = CharField(
        widget=TextInput(attrs={"placeholder": "Ingrese el nombre del denunciado"}),
    )
    apellidos_denunciado = CharField(
        widget=TextInput(attrs={"placeholder": "Ingrese el apellido del denunciado"}),
    )
    cedula_denunciado = CharField(
        max_length=12,
        required=False,
        label="Cédula del denunciado",
        widget=TextInput(attrs={"placeholder": "Ingrese la cédula del denunciado"}),
        validators=[validate_cedula],
    )
    telefono_denunciado = CharField(
        required=False,
        label="Teléfono del denunciado",
        widget=TextInput(attrs={"placeholder": "Ingrese el teléfono del denunciado"}),
    )
    email_denunciado = EmailField(
        max_length=60,
        required=False,
        label="Correo electrónico del denunciado",
        widget=EmailInput(
            attrs={"placeholder": "Ingrese el correo electrónico del denunciado"}
        ),
        validators=[validate_email],
    )
    direccion_denunciado = CharField(
        required=False,
        label="Dirección del denunciado",
        widget=TextInput(attrs={"placeholder": "Ingrese la dirección del denunciado"}),
    )

    class Meta:
        model = Denuncia
        fields = [
            "nombres_denunciante",
            "apellidos_denunciante",
            "cedula_denunciante",
            "telefono_denunciante",
            "email_denunciante",
            "direccion_denunciante",
            "nombres_denunciado",
            "apellidos_denunciado",
            "cedula_denunciado",
            "telefono_denunciado",
            "email_denunciado",
            "direccion_denunciado",
            "estatus",
            "ente",
            "motivo",
            "zona",
            "fecha_denuncia",
            "fecha_incidente",
        ]
        widgets = {
            "ente": TextInput(attrs={"placeholder": "Ingrese el ente relacionado"}),
            "zona": TextInput(attrs={"placeholder": "Ingrese la zona del incidente"}),
            "motivo": TextInput(
                attrs={"placeholder": "Ingrese el motivo de la denuncia"}
            ),
            "fecha_denuncia": DateInput(
                attrs={"placeholder": "Seleccione la fecha de denuncia", "type": "date"}
            ),
            "fecha_incidente": DateInput(
                attrs={
                    "placeholder": "Seleccione la fecha del incidente",
                    "type": "date",
                }
            ),
        }
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]
