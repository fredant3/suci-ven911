from potencia.uri.models import Uri
from django.forms import CharField, EmailField
from helpers.FormBase import FormBase
from django import forms


class UriInfoGeneralForm(FormBase):
    # 1) Informacion General
    # -Datos del servicio
    fecha_atencion = FormBase.create_date_field("fecha_atencion", "Fecha de Atención")
    nroreporte = CharField(
        max_length=10,
        required=False,
        label="Número de Reporte",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el número de reporte"}),
    )
    placa = CharField(
        max_length=10,
        required=False,
        label="Placa",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese la placa"}),
    )
    institucion = CharField(
        max_length=300,
        required=False,
        label="Institución",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese la institución"}),
    )
    num_interna = CharField(
        max_length=10,
        required=False,
        label="Numeración Interna",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese la numeración interna"}),
    )
    # Informacion Legal

    # Centro Asistencial Recibido
    centroAsistencial = CharField(
        max_length=50,
        required=False,
        label="Centro Asistencial",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el centro asistencial"}),
    )
    servicioAsistencial = CharField(
        max_length=50,
        required=False,
        label="Servicio Asistencial",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese el servicio asistencial"}
        ),
    )
    medico_receptor = CharField(
        max_length=50,
        required=False,
        label="Medico receptor",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el médico receptor"}),
    )

    msds = CharField(
        max_length=50,
        required=False,
        label="MS/DS",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese MS/DS"}),
    )

    # Registro Visuales

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
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]


class UripacienteForm(FormBase):
    # 2) Datos del paciente
    nombrepaciente = CharField(
        max_length=50,
        required=False,
        label="Nombre y Apellido del Paciente",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese nombre y apellido"}),
    )
    cedulapaciente = CharField(
        max_length=10,
        required=False,
        label="Cedula del Paciente",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese la cédula"}),
    )
    telefonopaciente = CharField(
        max_length=10,
        required=False,
        label="Numero de Telefono del Paciente",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el teléfono"}),
    )
    generopaciente = CharField(
        max_length=10,
        required=False,
        label="Genero del Paciente",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el género"}),
    )
    direccionpaciente = CharField(
        max_length=100,
        required=False,
        label="Direccion del paciente",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese la dirección"}),
    )
    # Autoridades presentes
    organismo = CharField(
        max_length=50,
        required=False,
        label="Nombre del Organismo",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el organismo"}),
    )
    jefedecomision = CharField(
        max_length=50,
        required=False,
        label="Jefe de Comision",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese jefe de comisión"}),
    )
    unidad_placa = CharField(
        max_length=10,
        required=False,
        label="Unidad/Placa",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese unidad/placa"}),
    )
    firma = CharField(
        max_length=10,
        required=False,
        label="Firma",
        widget=forms.TextInput(attrs={"placeholder": "Firma"}),
    )

    class Meta:
        model = Uri
        fields = (
            "nombrepaciente",
            "cedulapaciente",
            "telefonopaciente",
            "generopaciente",
            "direccionpaciente",
            "organismo",
            "jefedecomision",
            "unidad_placa",
            "firma",
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]


class UriConsentimientoForm(FormBase):
    #  Datos del acompañante
    nombre_acompanante = CharField(
        max_length=50,
        required=False,
        label="Nombre y Apellido del Acompañante",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese nombre y apellido"}),
    )
    parentezco_acompanante = CharField(
        max_length=10,
        required=False,
        label="Parentesco del Acompañante",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese parentesco"}),
    )
    cedula_acompanante = CharField(
        max_length=10,
        required=False,
        label="Cedula de Acompañante",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese la cédula"}),
    )
    telefono_acompanate = CharField(
        max_length=10,
        required=False,
        label="Telefono del Acompañante",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el teléfono"}),
    )
    genero_acompanante = CharField(
        max_length=10,
        required=False,
        label="Genero del Acompañante",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el género"}),
    )
    direccion_acompanante = CharField(
        max_length=100,
        required=False,
        label="Dirección del Acompañante",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese la dirección"}),
    )

    # Datos del testigo
    nombre_testigo = CharField(
        max_length=50,
        required=False,
        label="Nombre y Apellido del Testigo",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese nombre y apellido"}),
    )
    edad_testigo = forms.IntegerField(
        label="Edad Testigo",
        required=False,
        widget=forms.NumberInput(attrs={"placeholder": "Ingrese la edad"}),
    )
    cedula_testigo = CharField(
        max_length=10,
        required=False,
        label="Cedula del Testigo",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese la cédula"}),
    )
    telefono_testigo = CharField(
        max_length=10,
        required=False,
        label="Telefono del Testigo",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el teléfono"}),
    )
    direccion_testigo = CharField(
        max_length=100,
        required=False,
        label="Dirección del Acompañante",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese la dirección"}),
    )

    class Meta:
        model = Uri
        fields = (
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
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]

    # 4)Direccion Exacta del Evento


class UriDireccionForm(FormBase):
    estado_evento = CharField(
        max_length=20,
        required=False,
        label="Estado",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el estado"}),
    )
    municipio_evento = CharField(
        max_length=20,
        required=False,
        label="Municipio",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el municipio"}),
    )
    parroquia_evento = CharField(
        max_length=20,
        required=False,
        label="Parroquia",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese la parroquia"}),
    )
    sector_evento = CharField(
        max_length=100,
        required=False,
        label="Sector/Urbanizacion",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese sector/urbanización"}),
    )
    calle_evento = CharField(
        max_length=100,
        required=False,
        label="Calle/Avenida/Carretera",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese calle/avenida/carretera"}
        ),
    )
    casa_evento = CharField(
        max_length=100,
        required=False,
        label="Edificio/Casa/",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese edificio/casa"}),
    )
    piso_evento = CharField(
        max_length=100,
        required=False,
        label="Piso y Apto.",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese piso y apto."}),
    )
    referencia_evento = CharField(
        max_length=100,
        required=False,
        label="Punto de Referencia",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese punto de referencia"}),
    )
    eje_evento = CharField(
        max_length=30,
        required=False,
        label="Eje",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el eje"}),
    )

    # Cronologia del servicio

    hora_alarma = FormBase.create_time_field("Hora de Alarma")
    hora_salida = FormBase.create_time_field("Hora de Salida")
    hora_llegada = FormBase.create_time_field("Hora de Llegada")
    hospital = CharField(
        max_length=50,
        required=False,
        label="Llegada al Hospital",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese hospital"}),
    )
    transferencia_emergencia = CharField(
        max_length=20,
        required=False,
        label="Transferencia al Servicio de Emergencia",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese transferencia"}),
    )
    hora_sede = FormBase.create_time_field("Hora de Retorno a la Sede")
    tiempo_servicio = CharField(
        max_length=50,
        required=False,
        label="Tiempo de Servicio",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese tiempo de servicio"}),
    )
    observaciones_servicio = CharField(
        max_length=300,
        required=False,
        label="Observaciones del Servicio",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese observaciones"}),
    )

    class Meta:
        model = Uri
        fields = (
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


class UriInfoclinicaForm(FormBase):
    # 5) Informacion Clinica
    # Trauma
    observacionesSustancia = CharField(
        max_length=50,
        required=False,
        label="Observaciones de la sustancia",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese observaciones"}),
    )

    # Evaluacion Inicial + Intervenciones criticas

    # Via aerea o control cervical

    # 6) Respiracion, Oxigenacion y Circulacion

    # Respiracion y Oxigenacion

    descripcion_adic_resp = CharField(
        max_length=100,
        required=False,
        label="Descripción Adicional",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese descripción adicional"}),
    )

    # Circulacion

    # Deficit Neurologico

    ecgO = forms.IntegerField(
        required=False, widget=forms.NumberInput(attrs={"placeholder": "O"})
    )
    ecgV = forms.IntegerField(
        required=False, widget=forms.NumberInput(attrs={"placeholder": "V"})
    )
    ecgM = forms.IntegerField(
        required=False, widget=forms.NumberInput(attrs={"placeholder": "M"})
    )
    ecgTotal = forms.IntegerField(
        required=False, widget=forms.NumberInput(attrs={"placeholder": "Total"})
    )

    # Exposicion

    signosSintomas = CharField(
        max_length=100,
        required=False,
        label="Signos y Sintomas",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese signos y síntomas"}),
    )
    alergias = CharField(
        max_length=100,
        required=False,
        label="Alergias",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese alergias"}),
    )
    medicamentos = CharField(
        max_length=100,
        required=False,
        label="Medicamentos",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese medicamentos"}),
    )
    preexistencias = CharField(
        max_length=100,
        required=False,
        label="Preexistencias",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese preexistencias"}),
    )
    ultimaComida = CharField(
        max_length=100,
        required=False,
        label="Última comida",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese última comida"}),
    )
    evento = CharField(
        max_length=100,
        required=False,
        label="Evento",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese evento"}),
    )

    class Meta:
        model = Uri
        fields = (
            "accidenteVehicular",
            "enfrentamientoArmado",
            "traumaVehiculo",
            "viajaba",
            "sustanciaPeligrosa",
            "observacionesSustancia",
            "traumaNoIntencional",
            "emergenciaMedica",
            "hemorragia",
            "presion",
            "empaquetado",
            "torniquete",
            "evaluacion",
            "intervencion",
            "resultado",
            "descripcion_adic",
            "evaluacionResp",
            "intervencionResp",
            "resultadoResp",
            "descripcion_adic_resp",
            "colorPiel",
            "temperaturaPiel",
            "humedadPiel",
            "pulso",
            "otrasHerida",
            "fractura",
            "maniobraPelvis",
            "ecgO",
            "ecgV",
            "ecgM",
            "ecgTotal",
            "reaccionPupilar",
            "hipotermia",
            "signosSintomas",
            "alergias",
            "medicamentos",
            "preexistencias",
            "ultimaComida",
            "evento",
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]


class UriSignosVitalesForm(FormBase):
    # 7) Signos Vitales o Tratamiento

    # Signos Vitales

    horaMedicion = FormBase.create_time_field("Hora de la Medición")
    frecuenciaCardiaca = CharField(
        max_length=100,
        required=False,
        label="Frecuencia Cardiaca",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese frecuencia cardiaca"}),
    )
    frecuenciaRespiratoria = CharField(
        max_length=100,
        required=False,
        label="Frecuencia Respiratoria",
        widget=forms.TextInput(
            attrs={"placeholder": "Ingrese frecuencia respiratoria"}
        ),
    )
    presionArterial = CharField(
        max_length=100,
        required=False,
        label="Presión Arterial",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese presión arterial"}),
    )
    spo2 = CharField(
        max_length=100,
        required=False,
        label="SPO2",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese SPO2"}),
    )
    temperatura = CharField(
        max_length=100,
        required=False,
        label="Temperatura",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese temperatura"}),
    )
    llenadoCapilar = CharField(
        max_length=100,
        required=False,
        label="Llenado Capilar",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese llenado capilar"}),
    )
    glicemiaCapilar = CharField(
        max_length=100,
        required=False,
        label="Glicemia Capilar",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese glicemia capilar"}),
    )
    escalaGlasgow = CharField(
        max_length=100,
        required=False,
        label="Escala Glasgow",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese escala Glasgow"}),
    )

    # Tratamiento (opcion para añadir/ adicionar)
    medicamento = CharField(
        max_length=100,
        required=False,
        label="Medicamentos",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese medicamento"}),
    )
    dosis = CharField(
        max_length=100,
        required=False,
        label="Dosis",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese dosis"}),
    )
    hora = FormBase.create_time_field("Hora")
    resultadoEvaluacion = CharField(
        max_length=500,
        required=False,
        label="Resultados de la Evaluación Fisica Cefalo Caudal",
        widget=forms.Textarea(
            attrs={"placeholder": "Ingrese resultados de evaluación"}
        ),
    )

    class Meta:
        model = Uri
        fields = (
            "horaMedicion",
            "frecuenciaCardiaca",
            "frecuenciaRespiratoria",
            "presionArterial",
            "spo2",
            "temperatura",
            "llenadoCapilar",
            "glicemiaCapilar",
            "escalaGlasgow",
            "medicamento",
            "dosis",
            "hora",
            "resultadoEvaluacion",
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]


# Registro de Referencias y Contrareferencias
class UriReferenciasForm(FormBase):
    hospitalOrigen = CharField(
        max_length=100,
        required=False,
        label="Hospital de Origen",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese hospital de origen"}),
    )
    medicoRefiere = CharField(
        max_length=100,
        required=False,
        label="Medico que refiere",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese médico que refiere"}),
    )
    horaSalidaHosp = FormBase.create_time_field("Hora de Salida")
    hospitalDestino = CharField(
        max_length=100,
        required=False,
        label="Hospital que recibe",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese hospital destino"}),
    )
    horaLlegadaHosp = FormBase.create_time_field("Hora de Llegada")
    causa = CharField(
        max_length=100,
        required=False,
        label="Ingrese las causas",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese las causas"}),
    )
    tecnicoEmergencia = CharField(
        max_length=50,
        required=False,
        label="Técnico de emergencias médicas",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese técnico"}),
    )
    cedulaTecnico = CharField(
        max_length=10,
        required=False,
        label="Cédula del Técnico de emergencias médicas",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese cédula técnico"}),
    )
    tercerTripulante = CharField(
        max_length=50,
        required=False,
        label="Tercer Tripulante",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese tercer tripulante"}),
    )
    cedulaTripulante = CharField(
        max_length=10,
        required=False,
        label="Cédula del tercer tripulante",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese cédula tripulante"}),
    )
    conductorUnidad = CharField(
        max_length=50,
        required=False,
        label="Conductor de la unidad",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese conductor"}),
    )
    cedulaConductor = CharField(
        max_length=10,
        required=False,
        label="Cedula del conductor de la unidad",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese cédula conductor"}),
    )
    supervisorGuardia = CharField(
        max_length=50,
        required=False,
        label="Supervisor de Guardia",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese supervisor"}),
    )
    cedulaSupervisor = CharField(
        max_length=10,
        required=False,
        label="Cédula del Supervisor de Guardia",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese cédula supervisor"}),
    )
    medicoGuardia = CharField(
        max_length=50,
        required=False,
        label="Médico de Guardia",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese médico guardia"}),
    )
    cedulaMedico = CharField(
        max_length=10,
        required=False,
        label="Cédula del Médico de Guardia",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese cédula médico"}),
    )
    selloMsds = CharField(
        max_length=20,
        required=False,
        label="Sellos/MSDS",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese sellos/MSDS"}),
    )

    class Meta:
        model = Uri
        fields = (
            "trasladoIncial",
            "hospitalOrigen",
            "medicoRefiere",
            "horaSalidaHosp",
            "hospitalDestino",
            "horaLlegadaHosp",
            "causa",
            "tecnicoEmergencia",
            "cedulaTecnico",
            "tercerTripulante",
            "cedulaTripulante",
            "conductorUnidad",
            "cedulaConductor",
            "supervisorGuardia",
            "cedulaSupervisor",
            "medicoGuardia",
            "cedulaMedico",
            "selloMsds",
        )
        exclude = [
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
            "deleted_at",
            "deleted_by",
        ]
