from django.db import models
from django.forms import model_to_dict
from helpers.BaseModelMixin import BaseModel

ESTATUS_CHOICES = (
    ("noncontac", "No hubo contacto con el paciente"),  # Opciones:
    ("contac", "Si hubo contacto con el paciente"),  # Opciones:
)

ESTATUS_CHOICES2 = (
    ("positivo", "Si"),
    ("negativo", "No"),
)

ESTATUS_CHOICES3 = (
    ("casa", "Hogar"),
    ("escue", "Escuela"),
    ("calle", "Via Publica"),
    ("work", "Trabajo"),
)

ESTATUS_CHOICES4 = (
    ("ambula", "Ambulancia"),
    ("Vehi", "Vehiculo Particular"),
    ("noasist", "No Asistencial"),
    ("organ", "Organismo"),
)

ESTATUS_CHOICES5 = (
    ("rs", "RRSS"),
    ("rad", "Radio"),
    ("casu", "Casual"),
    ("telef", "Telefonico"),
    ("otr", "Otro"),
)

ESTATUS_CHOICES6 = (
    ("guardr", "Guardia de Rutina"),
    ("guardp", "Guardia de Prevencion"),
    ("interhosp", "Alta/Residencia/Interhospitalario"),
    ("apoy", "Apoyo"),
    ("otr", "Otro"),
)


class Uri(BaseModel):
    # 1) Informacion General
    # -Datos del servicio
    fecha_atencion = models.DateField(
        "Fecha de Atencion", max_length=10, blank=True, null=True
    )
    nroreporte = models.CharField(
        "Numero de Reporte", max_length=10, blank=True, null=True
    )
    placa = models.CharField("Placa", max_length=10, blank=True, null=True)
    institucion = models.CharField("Institucion", max_length=300, blank=True, null=True)
    tipounidad = models.CharField(
        "Tipo de Unidad", max_length=10, blank=True, null=True
    )
    num_interna = models.CharField(
        "Numeracion Interna", max_length=10, blank=True, null=True
    )
    # Informacion Legal
    contacto = models.CharField(
        "¿Hubo contacto con el paciente?", max_length=9, choices=ESTATUS_CHOICES
    )

    # Centro Asistencial Recibido
    centroAsistencial = models.CharField(max_length=50, blank=True, null=True)
    servicioAsistencial = models.CharField(max_length=50, blank=True, null=True)
    medico_receptor = models.CharField(max_length=50, blank=True, null=True)
    msds = models.CharField(max_length=50, blank=True, null=True)

    # Registro Visuales
    foto = models.CharField(
        "¿Hubo registro fotografico?", max_length=9, choices=ESTATUS_CHOICES2
    )
    # 2)Datos del paciente
    # Datos del paciente
    nombrepaciente = models.CharField(
        "Nombre y apellido del Paciente", max_length=50, blank=True, null=True
    )
    cedulapaciente = models.CharField(
        "Cedula del paciente", max_length=10, blank=True, null=True
    )
    telefonopaciente = models.CharField(
        "Numero de Telefono del Paciente", max_length=11, blank=True, null=True
    )
    generopaciente = models.CharField(
        "Genero del Paciente", max_length=10, blank=True, null=True
    )
    direccionpaciente = models.CharField(
        "Direccion del Paciente", max_length=300, blank=True, null=True
    )

    # Autoridades Presentes (Opcion de Añadir mas de un organismo)

    organismo = models.CharField(
        "Nombre del Organismo", max_length=20, blank=True, null=True
    )
    jefedecomision = models.CharField(
        "Jefe de Comision", max_length=50, blank=True, null=True
    )
    unidad_placa = models.CharField(
        "Unidad/Placa", max_length=20, blank=True, null=True
    )
    firma = models.CharField("Firma", max_length=20, blank=True, null=True)

    # 3) Consentimiento informado
    # Datos del acompañante
    nombre_acompanante = models.CharField(
        "Nombre del Acompañante", max_length=50, blank=True, null=True
    )
    parentezco_acompanante = models.CharField(
        "Parentesco del Acompañante", max_length=10, blank=True, null=True
    )
    cedula_acompanante = models.CharField(
        "Cedula del Acompañante", max_length=10, blank=True, null=True
    )
    telefono_acompanate = models.CharField(
        "Numero de Telefono del Acompañante", max_length=11, blank=True, null=True
    )
    genero_acompanante = models.CharField(
        "Genero del acompañante", max_length=10, blank=True, null=True
    )
    direccion_acompanante = models.CharField(
        "Direccion del acompañante", max_length=300, blank=True, null=True
    )

    # Datos del testigo
    nombre_testigo = models.CharField(
        "Nombre y Apellido del Testigo", max_length=50, blank=True, null=True
    )
    edad_testigo = models.IntegerField("Edad del Testigo", blank=True, null=True)
    cedula_testigo = models.CharField(
        "Cedula del testigo", max_length=10, blank=True, null=True
    )
    telefono_testigo = models.CharField(
        "Numero de Telefono del Testigo", max_length=11, blank=True, null=True
    )
    direccion_testigo = models.CharField(
        "Direccion del Testigo", max_length=300, blank=True, null=True
    )

    # 4)Direccion Exacta del Evento
    # Direccion
    estado_evento = models.CharField(
        "Estado", max_length=20, blank=True, null=True
    )  # Input Select
    municipio_evento = models.CharField(
        "Municipio", max_length=20, blank=True, null=True
    )
    parroquia_evento = models.CharField(
        "Parroquia", max_length=20, blank=True, null=True
    )
    sector_evento = models.CharField(
        "Sector/Urbanizacion", max_length=300, blank=True, null=True
    )
    calle_evento = models.CharField(
        "Calle/Avenida/Carrera", max_length=300, blank=True, null=True
    )
    casa_evento = models.CharField("Edif/ Casa", max_length=20, blank=True, null=True)
    piso_evento = models.CharField("Piso y Apto", max_length=20, blank=True, null=True)
    referencia_evento = models.CharField(
        "Punto de Referencia", max_length=300, blank=True, null=True
    )
    eje_evento = models.CharField("Eje", max_length=30, blank=True, null=True)

    lugar_atencion = models.CharField(
        "Lugar de Atención", max_length=9, choices=ESTATUS_CHOICES3
    )

    modo_traslado = models.CharField(
        "Modo de Traslado", max_length=9, choices=ESTATUS_CHOICES4
    )

    via_reporte = models.CharField(
        "Vía del Reporte", max_length=9, choices=ESTATUS_CHOICES5
    )

    servicio_tipo = models.CharField(
        "Tipo de Servicio", max_length=9, choices=ESTATUS_CHOICES6
    )

    # Cronologia del Servicio

    hora_alarma = models.TimeField("Hora de Alarma", blank=True, null=True)
    hora_salida = models.TimeField("Hora de Salida", blank=True, null=True)
    hora_llegada = models.TimeField("Hora de Llegada", blank=True, null=True)
    hospital = models.CharField(
        "Llegada al Hospital", max_length=50, blank=True, null=True
    )
    transferencia_emergencia = models.CharField(
        "Transferencia al Servicio de Emergencia", max_length=50, blank=True, null=True
    )
    hora_sede = models.TimeField("Hora de Retorno a la Sede", blank=True, null=True)
    tiempo_servicio = models.CharField(
        "Tiempo de Servicio", max_length=50, blank=True, null=True
    )
    observaciones_servicio = models.CharField(
        "Observaciones del Servicios", max_length=150, blank=True, null=True
    )

    # 5) Informacion Clinica
    # Trauma

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Unidad de repuesta inmediata"
        verbose_name_plural = "Unidades de repuestas inmediatas"
