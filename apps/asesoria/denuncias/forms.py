from asesoria.denuncias.models import Denuncia
from django import forms
from helpers.FormBase import FormBase
from helpers.validForm import (
    validate_nombres_apellidos,
    validate_cedula,
    validate_telefono,
    validate_email,
    validate_direccion,
    validate_general_text,
    validate_general_text,
    validate_general_text,
)


class DenunciaForm(FormBase):
    nombres_denunciante = forms.CharField(
        max_length=120,
        label="Nombre del denunciante",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese el nombre del denunciante"}
        ),
        validators=[validate_nombres_apellidos],
    )
    apellidos_denunciante = forms.CharField(
        max_length=120,
        label="Apellido del denunciante",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese el apellido del denunciante"}
        ),
        validators=[validate_nombres_apellidos],
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
        max_length=15,
        label="Teléfono del denunciante",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese el teléfono del denunciante"}
        ),
        validators=[validate_telefono],
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
        max_length=180,
        label="Dirección del denunciante",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese la dirección del denunciante"}
        ),
        validators=[validate_direccion],
    )

    nombres_denunciado = forms.CharField(
        max_length=120,
        required=False,
        label="Nombre del denunciado",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese el nombre del denunciado"}
        ),
        validators=[validate_nombres_apellidos],
    )
    apellidos_denunciado = forms.CharField(
        max_length=120,
        required=False,
        label="Apellido del denunciado",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese el apellido del denunciado"}
        ),
        validators=[validate_nombres_apellidos],
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
        max_length=15,
        required=False,
        label="Teléfono del denunciado",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese el teléfono del denunciado"}
        ),
        validators=[validate_telefono],
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
        max_length=180,
        required=False,
        label="Dirección del denunciado",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese la dirección del denunciado"}
        ),
        validators=[validate_direccion],
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
        max_length=120,
        label="Ente",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el ente relacionado"}),
        validators=[validate_general_text],
    )
    motivo = forms.CharField(
        max_length=120,
        label="Motivo",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese el motivo de la denuncia"}
        ),
        validators=[validate_general_text],
    )
    zona = forms.CharField(
        max_length=120,
        label="Zona del incidente",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese la zona del incidente"}),
        validators=[validate_general_text],
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
