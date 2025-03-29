from asesoria.denuncias.models import Denuncia
from django import forms
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_cedula,
    validate_email,
)


class DenunciaForm(FormBase):
    nombres_denunciante = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese el nombre del denunciante"}
        ),
    )
    apellidos_denunciante = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese el apellido del denunciante"}
        ),
    )
    cedula_denunciante = forms.CharField(
        max_length=12,
        label="Cédula del denunciante",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese la cédula del denunciante"}
        ),
        validators=[validate_cedula],
    )
    telefono_denunciante = forms.CharField(
        label="Teléfono del denunciante",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese el teléfono del denunciante"}
        ),
    )
    email_denunciante = forms.EmailField(
        max_length=60,
        required=False,
        label="Correo electrónico del denunciante",
        widget=forms.EmailInput(
            attrs={"placeholder": "Ingrese el correo electrónico del denunciante"}
        ),
        validators=[validate_email],
    )
    direccion_denunciante = forms.CharField(
        label="Dirección del denunciante",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese la dirección del denunciante"}
        ),
    )

    nombres_denunciado = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese el nombre del denunciado"}
        ),
    )
    apellidos_denunciado = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese el apellido del denunciado"}
        ),
    )
    cedula_denunciado = forms.CharField(
        max_length=12,
        required=False,
        label="Cédula del denunciado",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese la cédula del denunciado"}
        ),
        validators=[validate_cedula],
    )
    telefono_denunciado = forms.CharField(
        required=False,
        label="Teléfono del denunciado",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese el teléfono del denunciado"}
        ),
    )
    email_denunciado = forms.EmailField(
        max_length=60,
        required=False,
        label="Correo electrónico del denunciado",
        widget=forms.EmailInput(
            attrs={"placeholder": "Ingrese el correo electrónico del denunciado"}
        ),
        validators=[validate_email],
    )
    direccion_denunciado = forms.CharField(
        required=False,
        label="Dirección del denunciado",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese la dirección del denunciado"}
        ),
    )

    fecha_denuncia = forms.DateField(
        label="Fecha de denuncia",
        widget=forms.DateInput(
            attrs={"placeholder": "Seleccione la fecha de denuncia", "type": "date"}
        ),
    )
    fecha_incidente = forms.DateField(
        label="Fecha del incidente",
        widget=forms.DateInput(
            attrs={"placeholder": "Seleccione la fecha del incidente", "type": "date"}
        ),
    )

    ente = forms.CharField(
        label="Ente",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el ente relacionado"}),
    )
    motivo = forms.CharField(
        label="Motivo",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese el motivo de la denuncia"}
        ),
    )
    zona = forms.CharField(
        label="Zona del incidente",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese la zona del incidente"}),
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
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted",
            "deleted_at",
            "deleted_by",
        ]
