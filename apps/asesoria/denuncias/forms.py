from asesoria.denuncias.models import Denuncia
from django.forms import CharField, EmailField
from django.forms.fields import DateTimeInput
from helpers.FormBase import FormBase


class DenunciaForm(FormBase):
    nombres_denunciante = CharField(max_length=120, label="Nombre del denunciante")
    apellidos_denunciante = CharField(max_length=120, label="Apellido del denunciante")
    cedula_denunciante = CharField(max_length=12, label="Cédula del denunciante")
    telefono_denunciante = CharField(max_length=15, label="Teléfono del denunciante")
    email_denunciante = EmailField(
        max_length=60, required=False, label="Correo electrónico del denunciante"
    )
    direccion_denunciante = CharField(max_length=180, label="Dirección del denunciante")

    nombres_denunciado = CharField(
        max_length=120, required=False, label="Nombre del denunciado"
    )
    apellidos_denunciado = CharField(
        max_length=120, required=False, label="Apellido del denunciado"
    )
    cedula_denunciado = CharField(
        max_length=12, required=False, label="Cédula del denunciado"
    )
    telefono_denunciado = CharField(
        max_length=15, required=False, label="Teléfono del denunciado"
    )
    email_denunciado = EmailField(
        max_length=60, required=False, label="Correo electrónico del denunciado"
    )
    direccion_denunciado = CharField(
        max_length=180, required=False, label="Dirección del denunciado"
    )

    fecha_denuncia = FormBase.create_date_field("fecha_denuncia")
    fecha_incidente = FormBase.create_date_field("fecha_incidente")

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
