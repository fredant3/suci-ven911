from potencia.uri.models import Uri
from helpers.FormBase import FormBase
from django.forms.fields import DateTimeInput

# fecha_atencion = FormBase.create_date_field("fecha_atencion")


class UriForm(FormBase):
    class Meta:
        model = Uri
        fields = (
            "fecha_atencion",
            "nroreporte",
            "placa",
            "institucion",
            "tipounidad",
            "num_interna",
            "contacto",
            "centroAsistencial",
            "servicioAsistencial",
            "medico_receptor",
            "msds",
            "foto",
            "nombrepaciente",
            "cedulapaciente",
            "telefonopaciente",
            "generopaciente",
            "direccionpaciente",
            "organismo",
            "jefedecomision",
            "unidad_placa",
            "firma",
            "nombre_acompanante",
            "parentezco_acompanante",
            "cedula_acompanante",
            "telefono_acompanate",
            "genero_acompanante",
            "direccion_acompanante",
            "nombre_testigo",
            "edad_testigo",
            "cedula_testigo",
            "telefono_testigo",
            "direccion_testigo",
            "estado_evento",
            "municipio_evento",
            "parroquia_evento",
            "sector_evento",
            "calle_evento",
            "casa_evento",
            "piso_evento",
            "referencia_evento",
            "eje_evento",
            "lugar_atencion",
            "modo_traslado",
            "via_reporte",
            "servicio_tipo",
            "hora_alarma",
            "hora_salida",
            "hora_llegada",
            "hospital",
            "transferencia_emergencia",
            "hora_sede",
            "tiempo_servicio",
            "observaciones_servicio",
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]
