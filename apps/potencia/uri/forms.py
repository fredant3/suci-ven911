from potencia.uri.models import Uri
from django.forms import CharField, EmailField
from helpers.FormBase import FormBase
from django import forms


class UriInfoGeneralForm(FormBase):
    # 1) Informacion General
    # -Datos del servicio
    fecha_atencion = FormBase.create_date_field("fecha_atencion", "Fecha de Atención")
    nroreporte = CharField(max_length=10, required=False, label="Número de Reporte")
    placa = CharField(max_length=10, required=False, label="Número de Reporte")
    institucion = CharField(max_length=300, required=False, label="Institución")
    num_interna = CharField(max_length=10, required=False, label="Numeración Interna")
    # Informacion Legal

    # Centro Asistencial Recibido
    centroAsistencial = CharField(
        max_length=50, required=False, label="Centro Asistencial"
    )
    servicioAsistencial = CharField(
        max_length=50, required=False, label="Servicio Asistencial"
    )
    medico_receptor = CharField(max_length=50, required=False, label="Medico receptor")

    msds = CharField(max_length=50, required=False, label="MS/DS")

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
    # Datos del paciente
    nombrepaciente = CharField(
        max_length=50, required=False, label="Nombre y Apellido del Paciente"
    )
    cedulapaciente = CharField(
        max_length=10, required=False, label="Cedula del Paciente"
    )
    telefonopaciente = CharField(
        max_length=10, required=False, label="Numero de Telefono del Paciente"
    )
    generopaciente = CharField(
        max_length=10, required=False, label="Genero del Paciente"
    )
    direccionpaciente = CharField(
        max_length=100, required=False, label="Direccion del paciente"
    )

    # Autoridades presentes
    organismo = CharField(max_length=50, required=False, label="Nombre del Organismo")
    jefedecomision = CharField(max_length=50, required=False, label="Jefe de Comision")
    unidad_placa = CharField(max_length=10, required=False, label="Unidad/Placa")
    firma = CharField(max_length=10, required=False, label="Firma")


class UriConsentimientoForm(FormBase):
    # Datos del acompañante
    nombre_acompanante = CharField(
        max_length=50, required=False, label="Nombre y Apellido del Acompañante"
    )
    parentezco_acompanante = CharField(
        max_length=10, required=False, label="Parentesco del Acompañante"
    )
    cedula_acompanante = CharField(
        max_length=10, required=False, label="Cedula de Acompañante"
    )
    telefono_acompanate = CharField(
        max_length=10, required=False, label="Telefono del Acompañante"
    )
    genero_acompanante = CharField(
        max_length=10, required=False, label="Genero del Acompañante"
    )
    direccion_acompanante = CharField(
        max_length=100, required=False, label="Dirección del Acompañante"
    )

    # Datos del testigo
    nombre_testigo = CharField(
        max_length=50, required=False, label="Nombre y Apellido del Testigo"
    )
    edad_testigo = forms.IntegerField(label="Edad Testigo", required=False)
    cedula_testigo = CharField(
        max_length=10, required=False, label="Cedula del Testigo"
    )
    telefono_testigo = CharField(
        max_length=10, required=False, label="Telefono del Testigo"
    )
    direccion_testigo = CharField(
        max_length=100, required=False, label="Dirección del Acompañante"
    )

    # 4)Direccion Exacta del Evento


class UriDireccionForm(FormBase):

    estado_evento = CharField(max_length=20, required=False, label="Estado")
    municipio_evento = CharField(max_length=20, required=False, label="Municipio")
    parroquia_evento = CharField(max_length=20, required=False, label="Parroquia")
    sector_evento = CharField(
        max_length=100, required=False, label="Sector/Urbanizacion"
    )
    calle_evento = CharField(
        max_length=100, required=False, label="Calle/Avenida/Carretera"
    )
    casa_evento = CharField(max_length=100, required=False, label="Edificio/Casa/")
    piso_evento = CharField(max_length=100, required=False, label="Piso y Apto.")
    referencia_evento = CharField(
        max_length=100, required=False, label="Punto de Referencia"
    )
    eje_evento = CharField(max_length=30, required=False, label="Eje")

    # Cronologia del servicio

    hora_alarma = FormBase.create_time_field("Hora de Alarma")
    hora_salida = FormBase.create_time_field("Hora de Salida")
    hora_llegada = FormBase.create_time_field("Hora de Llegada")
    hospital = CharField(max_length=50, required=False, label="Llegada al Hospital")
    transferencia_emergencia = CharField(
        max_length=20, required=False, label="Transferencia al Servicio de Emergencia"
    )
    hora_sede = FormBase.create_time_field("Hora de Retorno a la Sede")
    tiempo_servicio = CharField(
        max_length=50, required=False, label="Tiempo de Servicio"
    )
    observaciones_servicio = CharField(
        max_length=300, required=False, label="Observaciones del Servicio"
    )


class UriInfoclinicaForm(FormBase):
    # 5) Informacion Clinica
    # Trauma

    observacionesSustancia = CharField(
        max_length=50, required=False, label="Observaciones de la sustancia"
    )

    # Evaluacion Inicial + Intervenciones criticas

    # Via aerea o control cervical

    # 6) Respiracion, Oxigenacion y Circulacion

    # Respiracion y Oxigenacion

    descripcion_adic_resp = CharField(
        max_length=100, required=False, label="Descripción Adicional"
    )

    # Circulacion

    # Deficit Neurologico

    ecgO = forms.IntegerField(required=False)
    ecgV = forms.IntegerField(required=False)
    ecgM = forms.IntegerField(required=False)
    ecgTotal = forms.IntegerField(required=False)

    # Exposicion

    signosSintomas = CharField(
        max_length=100, required=False, label="Signos y Sintomas"
    )
    alergias = CharField(max_length=100, required=False, label="Alergias")
    medicamentos = CharField(max_length=100, required=False, label="Medicamentos")
    preexistencias = CharField(max_length=100, required=False, label="Preexistencias")
    ultimaComida = CharField(max_length=100, required=False, label="Última comida")
    evento = CharField(max_length=100, required=False, label="Evento")


class UriSignosVitalesForm(FormBase):
    # 7) Signos Vitales o Tratamiento

    # Signos Vitales

    horaMedicion = FormBase.create_time_field("Hora de la Medición")
    frecuenciaCardiaca = CharField(
        max_length=100, required=False, label="Frecuencia Cardiaca"
    )
    frecuenciaRespiratoria = CharField(
        max_length=100, required=False, label="Frecuencia Respiratoria"
    )
    presionArterial = CharField(
        max_length=100, required=False, label="Presión Arterial"
    )
    spo2 = CharField(max_length=100, required=False, label="SPO2")
    temperatura = CharField(max_length=100, required=False, label="Temperatura")
    llenadoCapilar = CharField(max_length=100, required=False, label="Llenado Capilar")
    glicemiaCapilar = CharField(
        max_length=100, required=False, label="Glicemia Capilar"
    )
    escalaGlasgow = CharField(max_length=100, required=False, label="Escala Glasgow")

    # Tratamiento (opcion para añadir/ adicionar)
    medicamento = CharField(max_length=100, required=False, label="Medicamentos")
    dosis = CharField(max_length=100, required=False, label="Dosis")
    hora = FormBase.create_time_field("Hora")
    resultadoEvaluacion = CharField(
        max_length=500,
        required=False,
        label="Resultados de la Evaluación Fisica Cefalo Caudal",
    )

    # Registro de Referencias y Contrareferencias


class UriReferenciasForm(FormBase):
    hospitalOrigen = CharField(
        max_length=100, required=False, label="Hospital de Origen"
    )
    medicoRefiere = CharField(
        max_length=100, required=False, label="Medico que refiere"
    )
    horaSalidaHosp = FormBase.create_time_field("Hora de Salida")
    hospitalDestino = CharField(
        max_length=100, required=False, label="Hospital que recibe"
    )
    horaLlegadaHosp = FormBase.create_time_field("Hora de Llegada")
    causa = CharField(max_length=100, required=False, label="Ingrese las causas")
    tecnicoEmergencia = CharField(
        max_length=50, required=False, label="Técnico de emergencias médicas"
    )
    cedulaTecnico = CharField(
        max_length=10, required=False, label="Cédula del Técnico de emergencias médicas"
    )
    tercerTripulante = CharField(
        max_length=50, required=False, label="Tercer Tripulante"
    )
    cedulaTripulante = CharField(
        max_length=10, required=False, label="Cédula del tercer tripulante"
    )
    conductorUnidad = CharField(
        max_length=50, required=False, label="Conductor de la unidad"
    )
    cedulaConductor = CharField(
        max_length=10, required=False, label="Cedula del conductor de la unidad"
    )
    supervisorGuardia = CharField(
        max_length=50, required=False, label="Supervisor de Guardia"
    )
    cedulaSupervisor = CharField(
        max_length=10, required=False, label="Cédula del Supervisor de Guardia"
    )
    medicoGuardia = CharField(max_length=50, required=False, label="Médico de Guardia")
    cedulaMedico = CharField(
        max_length=10, required=False, label="Cédula del Médico de Guardia"
    )
    selloMsds = CharField(max_length=20, required=False, label="Sellos/MSDS")

    # edad_testigo = forms.IntegerField(label="Edad Testigo", required=False)

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
