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

ESTATUS_CHOICES7 = (
    ("conduc", "Conductor"),
    ("tripul", "Tripulante"),
)

ESTATUS_CHOICES8 = (
    ("caipie", "Caida de Propio Pie"),
    ("caialtu", "Caida de Altura"),
    ("quemad", "Quemadura"),
    ("morde", "Mordedura"),
    ("otr", "Otros"),
)

ESTATUS_CHOICES9 = (
    ("aler", "Alergias"),
    ("cefa", "Cefalea"),
    ("tension", "Hipo/Hipertensión"),
    ("gine", "Gineco-obstetrica"),
    ("conoci", "Perdida de Conocimiento"),
    ("disne", "Disnea/Dificultad Respiratoria"),
    ("dolo", "Dolor"),
    ("emes", "Emesis"),
    ("intox", "Intoxicaciones"),
    ("shock", "Shock no traumatico"),
    ("inme", "Inmersión"),
    ("sca", "SCA"),
    ("parad", "Parada Cardio Respiratoria"),
    ("convul", "Convulsiones"),
    ("hemor", "Hemorragias no traumaticas"),
    ("otro", "Otros"),
)

ESTATUS_CHOICES10 = (
    ("conscie", "Consciente"),
    ("inconsc", "Inconsciente"),
    ("viaperme", "V. A. Permeable"),
    ("vianope", "V. A. No Permeable"),
    ("ovac", "OVACE"),
    ("liquid", "Liquidos/Fluidos"),
    ("ruido", "Ruidos en V. A."),
    ("rme1", "Necesita RME"),
)

ESTATUS_CHOICES11 = (
    ("freme", "Frente-Menton"),
    ("tracc", "Tracción Mandibular"),
    ("succ", "Succión"),
    ("rme2", "RME"),
    ("cof", "COF"),
    ("cnf", "CNF"),
    ("dgs", "DSG/TET"),
    ("vaq", "VAQ"),
)

ESTATUS_CHOICES12 = (
    ("vaperme", "V. A. Permeabilizada"),
    ("vadeso", "V. A. Desobstruida"),
    ("movesp", "Mov. Esp. Restrigida"),
    ("vaisla", "V. A. Aislada/Asegurada"),
)

ESTATUS_CHOICES13 = (
    ("resp", "Respira/FR"),
    ("noresp", "No Respira"),
    ("Expsim", "Expansión Simetrica"),
    ("expasi", "Expansión Asimétrica"),
    ("esresp", "Esfuerzo Resp. Visible"),
    ("heris", "Herida Succionante"),
    ("estig", "Estigma de Trauma"),
    ("desvit", "Desviación Traqueal"),
    ("ingur", "Ingurgitación Yugular"),
    ("crepo", "Crepitantes (óseos)"),
    ("dolo", "Dolor"),
    ("enfi", "Enfisema S.C"),
    ("reso", "Resonancia"),
    ("hipere", "Hiper-resonancia"),
    ("mati", "Matidez"),
    ("murmu", "Murmullo Vesicular"),
    ("ronc", "Roncus"),
    ("sibi", "Sibilancias"),
    ("crepi", "Crepitantes"),
    ("aboli", "Abolición/Disminución RR"),
)

ESTATUS_CHOICES14 = (
    ("ventb", "Venta. Boca-Barr-Boca"),
    ("ventco", "Venta. Con BVM"),
    ("ventim", "Ventilación Mecánica"),
    ("valv", "Valvula de una vía"),
    ("parch", "Parche Oclusivo"),
    ("descom", "Descomp. por Aguja"),
    ("oxige", "Oxigenoterapia"),
    ("disp", "Dispositivo"),
    ("lpm", "LPM"),
    ("otr", "Otro"),
)

ESTATUS_CHOICES15 = (
    ("venties", "Ventila espontáneamente"),
    ("ventia", "Ventila con Asistencia"),
    ("neumot", "Neumotorax resuelto (Abierto o a tensión)"),
    ("aliv", "Alivio de la disnea (de origen no traumático)"),
)

ESTATUS_CHOICES16 = (
    ("pali", "Pálido"),
    ("norm", "Normal"),
)


ESTATUS_CHOICES17 = (
    ("fria", "Fría"),
    ("tibi", "Tibia"),
)

ESTATUS_CHOICES18 = (
    ("sec", "Seca"),
    ("hume", "Húmeda"),
)

ESTATUS_CHOICES19 = (
    ("isoc", "Isocórica"),
    ("anis", "Anisocoria"),
    ("mios", "Miosis"),
    ("midri", "Midriasis"),
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
        "¿Hubo contacto con el paciente?",
        max_length=9,
        choices=ESTATUS_CHOICES,
        blank=True,
        null=True,
    )

    # Centro Asistencial Recibido
    centroAsistencial = models.CharField(max_length=50, blank=True, null=True)
    servicioAsistencial = models.CharField(max_length=50, blank=True, null=True)
    medico_receptor = models.CharField(max_length=50, blank=True, null=True)
    msds = models.CharField(max_length=50, blank=True, null=True)

    # Registro Visuales
    foto = models.CharField(
        "¿Hubo registro fotografico?",
        max_length=9,
        choices=ESTATUS_CHOICES2,
        blank=True,
        null=True,
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
        "Lugar de Atención",
        max_length=9,
        choices=ESTATUS_CHOICES3,
        blank=True,
        null=True,
    )

    modo_traslado = models.CharField(
        "Modo de Traslado",
        max_length=9,
        choices=ESTATUS_CHOICES4,
        blank=True,
        null=True,
    )

    via_reporte = models.CharField(
        "Vía del Reporte", max_length=9, choices=ESTATUS_CHOICES5, blank=True, null=True
    )

    servicio_tipo = models.CharField(
        "Tipo de Servicio",
        max_length=9,
        choices=ESTATUS_CHOICES6,
        blank=True,
        null=True,
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
    accidenteVehicular = models.CharField(
        "Accidente Vehicular",
        max_length=9,
        choices=ESTATUS_CHOICES2,
        blank=True,
        null=True,
    )  # opciones: (colision, volcamiento, Embarracamiento, Choque, Arrollamiento, otro )
    enfrentamientoArmado = models.CharField(
        "Enfrentamiento Armado",
        max_length=9,
        choices=ESTATUS_CHOICES2,
        blank=True,
        null=True,
    )  # si es si, activar opciones "Tipo de Arma" (Blanca, Fuego, Biologica, Quimica, Otro)
    # tipoArma=models.ForeignKey(Tipo_arma, on_delete=models.CASCADE, blank=True, null=True)
    traumaVehiculo = models.CharField(
        "Trauma con Vehiculo",
        max_length=9,
        choices=ESTATUS_CHOICES2,
        blank=True,
        null=True,
    )  # si es si, activar opciones "Tipo de Vehiculo" (Automovil/Carro, Moto, Maquinaria, Otro)
    viajaba = models.CharField(
        "Viajaba como", max_length=9, choices=ESTATUS_CHOICES7, blank=True, null=True
    )
    sustanciaPeligrosa = models.CharField(
        "Sustancia Peligrosa",
        max_length=9,
        choices=ESTATUS_CHOICES2,
        blank=True,
        null=True,
    )  # si es si, activar opcion si es inflamable o explosivo)
    # inflamable = models.BooleanField()
    # explosivo = models.BooleanField()
    observacionesSustancia = models.CharField(
        "Observaciones de la sustancia",
        max_length=100,
        blank=True,
        null=True,
    )
    traumaNoIntencional = models.CharField(
        "Trauma no Intencional",
        max_length=9,
        choices=ESTATUS_CHOICES8,
        blank=True,
        null=True,
    )
    emergenciaMedica = models.CharField(
        "Emergencias Médicas no Traumáticas",
        max_length=9,
        choices=ESTATUS_CHOICES9,
        blank=True,
        null=True,
    )

    # Evaluacion Inicial + Intervenciones criticas

    hemorragia = models.CharField(
        "Hemorragias", max_length=9, choices=ESTATUS_CHOICES2, blank=True, null=True
    )
    presion = models.CharField(
        "Presión Directa", max_length=9, choices=ESTATUS_CHOICES2, blank=True, null=True
    )
    empaquetado = models.CharField(
        "Empaquetado de la Herida",
        max_length=9,
        choices=ESTATUS_CHOICES2,
        blank=True,
        null=True,
    )
    torniquete = models.CharField(
        "Torniquete", max_length=9, choices=ESTATUS_CHOICES2, blank=True, null=True
    )

    # Via aerea o control cervical

    evaluacion = models.CharField(
        "Evaluación", max_length=9, choices=ESTATUS_CHOICES10, blank=True, null=True
    )
    intervencion = models.CharField(
        "Intervenciones", max_length=9, choices=ESTATUS_CHOICES11, blank=True, null=True
    )
    resultado = models.CharField(
        "Resultados", max_length=9, choices=ESTATUS_CHOICES12, blank=True, null=True
    )
    descripcion_adic = models.CharField(
        "Descripción Adicional", max_length=100, blank=True, null=True
    )

    # 6) Respiracion, Oxigenacion y Circulacion

    # Respiracion y Oxigenacion

    evaluacionResp = models.CharField(
        "Evaluación", max_length=20, choices=ESTATUS_CHOICES13, blank=True, null=True
    )
    intervencionResp = models.CharField(
        "Intervención", max_length=20, choices=ESTATUS_CHOICES14, blank=True, null=True
    )
    resultadoResp = models.CharField(
        "Resultado", max_length=20, choices=ESTATUS_CHOICES15, blank=True, null=True
    )
    descripcion_adic_resp = models.CharField(
        "Descripción Adicional", max_length=100, blank=True, null=True
    )

    # Circulacion
    colorPiel = models.CharField(
        "Color de la Piel",
        max_length=9,
        choices=ESTATUS_CHOICES16,
        blank=True,
        null=True,
    )
    temperaturaPiel = models.CharField(
        "Temperatura de la Piel",
        max_length=9,
        choices=ESTATUS_CHOICES17,
        blank=True,
        null=True,
    )
    humedadPiel = models.CharField(
        "Humedad de la Piel",
        max_length=9,
        choices=ESTATUS_CHOICES18,
        blank=True,
        null=True,
    )
    pulso = models.CharField(
        "Pulsos distales", max_length=9, choices=ESTATUS_CHOICES2, blank=True, null=True
    )
    otrasHerida = models.CharField(
        "Otras hemorro/heridas",
        max_length=9,
        choices=ESTATUS_CHOICES2,
        blank=True,
        null=True,
    )
    fractura = models.CharField(
        "Fracturas", max_length=9, choices=ESTATUS_CHOICES2, blank=True, null=True
    )
    maniobraPelvis = models.CharField(
        "Maniobra de Pelvis",
        max_length=9,
        choices=ESTATUS_CHOICES2,
        blank=True,
        null=True,
    )

    # Deficit Neurologico
    ecgO = models.IntegerField(blank=True, null=True)
    ecgV = models.IntegerField(blank=True, null=True)
    ecgM = models.IntegerField(blank=True, null=True)
    ecgTotal = models.IntegerField(blank=True, null=True)
    reaccionPupilar = models.CharField(
        "Reacción Pupilar",
        max_length=9,
        choices=ESTATUS_CHOICES19,
        blank=True,
        null=True,
    )

    # Exposicion
    hipotermia = models.CharField(
        "Hipotermia", max_length=9, choices=ESTATUS_CHOICES2, blank=True, null=True
    )  # Opciones si es positivo (Menta Termica, Admini de liq tibios EV, otras lesiones)
    signosSintomas = models.CharField(
        "Signos y Sintomas", max_length=100, blank=True, null=True
    )
    alergias = models.CharField("Alergias", max_length=100, blank=True, null=True)
    medicamentos = models.CharField(
        "Medicamentos", max_length=100, blank=True, null=True
    )
    preexistencias = models.CharField(
        "Preexistencias", max_length=100, blank=True, null=True
    )
    ultimaComida = models.CharField(
        "Última comida", max_length=100, blank=True, null=True
    )
    evento = models.CharField("Evento", max_length=100, blank=True, null=True)

    # 7) Signos Vitales o Tratamiento

    # Signos Vitales
    horaMedicion = models.CharField(
        "Hora de la Medición", max_length=100, blank=True, null=True
    )
    frecuenciaCardiaca = models.CharField(
        "Frecuencia Cardiaca", max_length=100, blank=True, null=True
    )
    frecuenciaRespiratoria = models.CharField(
        "Frecuencia Respiratoria", max_length=100, blank=True, null=True
    )
    presionArterial = models.CharField(
        "Presión Arterial", max_length=100, blank=True, null=True
    )
    spo2 = models.CharField("SPO2", max_length=100, blank=True, null=True)
    temperatura = models.CharField("Temperatura", max_length=100, blank=True, null=True)
    llenadoCapilar = models.CharField(
        "Llenado Capilar", max_length=100, blank=True, null=True
    )
    glicemiaCapilar = models.CharField(
        "Glicemia Capillar", max_length=100, blank=True, null=True
    )
    escalaGlasgow = models.CharField(
        "Escala Glasgow", max_length=100, blank=True, null=True
    )

    # Tratamiento (opcion para añadir/ adicionar)
    medicamento = models.CharField("Medicamento", max_length=100, blank=True, null=True)
    dosis = models.CharField("Dosis", max_length=100, blank=True, null=True)
    hora = models.TimeField("Hora", blank=True, null=True)
    resultadoEvaluacion = models.CharField(
        "Resultados de la Evaluación Fisica Cefalo Caudal",
        max_length=500,
        blank=True,
        null=True,
    )

    # Registro de Referencias y Contrareferencias

    trasladoIncial = models.CharField(
        "¿El paciente fue referido del centro asistencial al que fue trasladado inicialmente?",
        max_length=9,
        choices=ESTATUS_CHOICES2,
        blank=True,
        null=True,
    )
    hospitalOrigen = models.CharField(
        "Hospital Origen", max_length=100, blank=True, null=True
    )
    medicoRefiere = models.CharField(
        "Medico que refiere", max_length=100, blank=True, null=True
    )
    horaSalidaHosp = models.TimeField("Hora de Salida", blank=True, null=True)
    hospitalDestino = models.CharField(
        "Hospital que recibe", max_length=100, blank=True, null=True
    )
    horaLlegadaHosp = models.TimeField("Hora de llegada", blank=True, null=True)
    causa = models.CharField(
        "Ingreses las causas", max_length=100, blank=True, null=True
    )
    tecnicoEmergencia = models.CharField(
        "Técnico de emergencias médicas", max_length=50, blank=True, null=True
    )
    cedulaTecnico = models.CharField(
        "Cédula del Técnico de emergencias médicas",
        max_length=10,
        blank=True,
        null=True,
    )
    tercerTripulante = models.CharField(
        "Tercer Tripulante", max_length=50, blank=True, null=True
    )
    cedulaTripulante = models.CharField(
        "Cédula del tercer tripulante", max_length=10, blank=True, null=True
    )
    conductorUnidad = models.CharField(
        "Conductor de la unidad", max_length=50, blank=True, null=True
    )
    cedulaConductor = models.CharField(
        "Cedula del conductor de la unidad", max_length=10, blank=True, null=True
    )
    supervisorGuardia = models.CharField(
        "Supervisor de Guardia", max_length=50, blank=True, null=True
    )
    cedulaSupervisor = models.CharField(
        "Cédula del Supervisor de Guardia", max_length=10, blank=True, null=True
    )
    medicoGuardia = models.CharField(
        "Médico de Guardia", max_length=50, blank=True, null=True
    )
    cedulaMedico = models.CharField(
        "Cédula del Médico de Guardia", max_length=10, blank=True, null=True
    )
    selloMsds = models.CharField("Sellos/MSDS", max_length=25, blank=True, null=True)
    permissions = [
        ("listar_uri", "Puede listar uri"),
        ("agregar_uri", "Puede agregar uri"),
        ("ver_uri", "Puede ver uri"),
        ("editar_uri", "Puede actualizar uri"),
        ("eliminar_uri", "Puede eliminar uri"),
    ]

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Unidad de repuesta inmediata"
        verbose_name_plural = "Unidades de repuestas inmediatas"
