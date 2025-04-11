import django.core.validators
import helpers.validForm
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Accion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_by",
                    models.CharField(max_length=6, verbose_name="Creado por"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado el"),
                ),
                (
                    "updated_by",
                    models.CharField(max_length=6, verbose_name="Actualizado por"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Actualizado el"),
                ),
                (
                    "deleted_by",
                    models.CharField(
                        blank=True,
                        max_length=6,
                        null=True,
                        verbose_name="Eliminado por",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Eliminado el"
                    ),
                ),
                (
                    "proyecto",
                    models.CharField(
                        max_length=64, verbose_name="Nombre del Proyecto:"
                    ),
                ),
                ("fecha_inicio", models.DateField(verbose_name="Fecha de Inicio")),
                (
                    "fecha_culminacion",
                    models.DateField(verbose_name="Fecha de Culminación"),
                ),
                (
                    "situacion_presupuestaria",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(6),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.UnicodeAlphaSpaceValidator(),
                        ],
                        verbose_name="Situación Presupuestaria:",
                    ),
                ),
                (
                    "monto",
                    models.CharField(max_length=64, verbose_name="Monto asignado:"),
                ),
                (
                    "responsable_gerente",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(6),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.TextValidator(),
                        ],
                        verbose_name="Responsable Gerente:",
                    ),
                ),
                (
                    "responsable_tecnico",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(6),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.TextValidator(),
                        ],
                        verbose_name="Responsable Técnico:",
                    ),
                ),
                (
                    "responsable_registrador",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(6),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.TextValidator(),
                        ],
                        verbose_name="Responsable Registrador:",
                    ),
                ),
                (
                    "responsable_administrativo",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(6),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.TextValidator(),
                        ],
                        verbose_name="Responsable Administrativo:",
                    ),
                ),
                (
                    "estatus",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(6),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.TextValidator(),
                        ],
                        verbose_name="Estatus del Proyecto:",
                    ),
                ),
            ],
            options={
                "verbose_name": "Accion",
                "verbose_name_plural": "Acciones",
                "permissions": [
                    ("listar_accion", "Puede listar acciones"),
                    ("agregar_accion", "Puede agregar accion"),
                    ("ver_accion", "Puede ver accion"),
                    ("editar_accion", "Puede actualizar accion"),
                    ("eliminar_accion", "Puede eliminar accion"),
                    ("pdf_accion", "Puede generar pdf de accion"),
                ],
            },
        ),
        migrations.CreateModel(
            name="Asignacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_by",
                    models.CharField(max_length=6, verbose_name="Creado por"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado el"),
                ),
                (
                    "updated_by",
                    models.CharField(max_length=6, verbose_name="Actualizado por"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Actualizado el"),
                ),
                (
                    "deleted_by",
                    models.CharField(
                        blank=True,
                        max_length=6,
                        null=True,
                        verbose_name="Eliminado por",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Eliminado el"
                    ),
                ),
                (
                    "departamento",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(4),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.TextValidator(),
                        ],
                        verbose_name="Nombre de la dirección",
                    ),
                ),
                (
                    "presupuesto",
                    models.CharField(
                        max_length=64, verbose_name="Presupuesto asignado"
                    ),
                ),
                (
                    "objetivo",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(4),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.TextValidator(),
                        ],
                        verbose_name="Objetivo general anual",
                    ),
                ),
                (
                    "numero_partida",
                    models.CharField(
                        max_length=10,
                        validators=[
                            django.core.validators.MinLengthValidator(2),
                            django.core.validators.MaxLengthValidator(10),
                            helpers.validForm.UnicodeAlphaSpaceValidator(
                                extra_chars="-"
                            ),
                        ],
                        verbose_name="Número de partida presupuestaria",
                    ),
                ),
            ],
            options={
                "verbose_name": "Asignacion",
                "verbose_name_plural": "Asignaciones",
                "permissions": [
                    ("listar_asignar_presupuesto", "Puede listar asignaciones"),
                    ("agregar_asignar_presupuesto", "Puede agregar asignacion"),
                    ("ver_asignar_presupuesto", "Puede ver asignacion"),
                    ("editar_asignar_presupuesto", "Puede actualizar asignacion"),
                    ("eliminar_asignar_presupuesto", "Puede eliminar asignacion"),
                    ("pdf_asignar_presupuesto", "Puede generar pdf de asignacion"),
                ],
            },
        ),
        migrations.CreateModel(
            name="Cedente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_by",
                    models.CharField(max_length=6, verbose_name="Creado por"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado el"),
                ),
                (
                    "updated_by",
                    models.CharField(max_length=6, verbose_name="Actualizado por"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Actualizado el"),
                ),
                (
                    "deleted_by",
                    models.CharField(
                        blank=True,
                        max_length=6,
                        null=True,
                        verbose_name="Eliminado por",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Eliminado el"
                    ),
                ),
                (
                    "idc",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.MinLengthValidator(4),
                            django.core.validators.MaxLengthValidator(255),
                            helpers.validForm.UnicodeAlphaSpaceValidator(
                                extra_chars="-"
                            ),
                        ],
                        verbose_name="Identificador Cedente:",
                    ),
                ),
                (
                    "partidac",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(4),
                            django.core.validators.MaxLengthValidator(255),
                            helpers.validForm.UnicodeAlphaSpaceValidator(
                                extra_chars="-"
                            ),
                        ],
                        verbose_name="Partida Contable",
                    ),
                ),
                (
                    "generalc",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxLengthValidator(255),
                            helpers.validForm.PositiveIntegerValidator(),
                        ],
                        verbose_name="General",
                    ),
                ),
                (
                    "espefc",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxLengthValidator(255),
                            helpers.validForm.PositiveIntegerValidator(),
                        ],
                        verbose_name="Específicaciones",
                    ),
                ),
                (
                    "subespefc",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxLengthValidator(255),
                            helpers.validForm.PositiveIntegerValidator(),
                        ],
                        verbose_name="Sub-Especialidad",
                    ),
                ),
                (
                    "denomc",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(4),
                            django.core.validators.MaxLengthValidator(255),
                            helpers.validForm.TextValidator(),
                        ],
                        verbose_name="Denominación",
                    ),
                ),
                (
                    "presuacorc",
                    models.CharField(
                        max_length=64, verbose_name="Presupuesto asignado"
                    ),
                ),
                (
                    "caufechac",
                    models.CharField(max_length=64, verbose_name="Causado a la fecha"),
                ),
                (
                    "dispc",
                    models.CharField(max_length=64, verbose_name="Disponible a causar"),
                ),
                (
                    "montocc",
                    models.CharField(max_length=64, verbose_name="Monto comprometido"),
                ),
                (
                    "saldofc",
                    models.CharField(max_length=64, verbose_name="Saldo final"),
                ),
                (
                    "direccionc",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(4),
                            django.core.validators.MaxLengthValidator(255),
                            helpers.validForm.TextValidator(),
                        ],
                        verbose_name="Dirección cedente",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cedente",
                "verbose_name_plural": "Cedentes",
                "permissions": [
                    ("listar_cedente", "Puede listar cedente"),
                    ("agregar_cedente", "Puede agregar cedente"),
                    ("ver_cedente", "Puede ver cedente"),
                    ("editar_cedente", "Puede actualizar cedente"),
                    ("eliminar_cedente", "Puede eliminar cedente"),
                    ("pdf_cedente", "Puede generar pdf de cedente"),
                ],
            },
        ),
        migrations.CreateModel(
            name="Proyecto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_by",
                    models.CharField(max_length=6, verbose_name="Creado por"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado el"),
                ),
                (
                    "updated_by",
                    models.CharField(max_length=6, verbose_name="Actualizado por"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Actualizado el"),
                ),
                (
                    "deleted_by",
                    models.CharField(
                        blank=True,
                        max_length=6,
                        null=True,
                        verbose_name="Eliminado por",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Eliminado el"
                    ),
                ),
                (
                    "nombrep",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(4),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.TextValidator(),
                        ],
                        verbose_name="Nombre del Proyecto",
                    ),
                ),
                ("fechai", models.DateField(verbose_name="Fecha de Inicio")),
                ("fechac", models.DateField(verbose_name="Fecha de Culminación")),
                (
                    "situacionp",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(4),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.UnicodeAlphaSpaceValidator(),
                        ],
                        verbose_name="Situación Presupuestaria",
                    ),
                ),
                (
                    "montoproyecto",
                    models.CharField(
                        max_length=64, verbose_name="Monto Total del Proyecto"
                    ),
                ),
                (
                    "responsableg",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(4),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.UnicodeAlphaSpaceValidator(),
                        ],
                        verbose_name="Responsable Gerente",
                    ),
                ),
                (
                    "responsablet",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(4),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.UnicodeAlphaSpaceValidator(),
                        ],
                        verbose_name="Responsable Técnico",
                    ),
                ),
                (
                    "responsabler",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(4),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.UnicodeAlphaSpaceValidator(),
                        ],
                        verbose_name="Responsable Registrador",
                    ),
                ),
                (
                    "responsablea",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(4),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.UnicodeAlphaSpaceValidator(),
                        ],
                        verbose_name="Responsable Administrativo",
                    ),
                ),
                (
                    "estatus",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(4),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.TextValidator(),
                        ],
                        verbose_name="Estatus del Proyecto",
                    ),
                ),
            ],
            options={
                "verbose_name": "Proyecto",
                "verbose_name_plural": "Proyectos",
                "permissions": [
                    ("listar_proyecto", "Puede listar proyectos"),
                    ("agregar_proyecto", "Puede agregar proyecto"),
                    ("ver_proyecto", "Puede ver proyecto"),
                    ("editar_proyecto", "Puede actualizar proyecto"),
                    ("eliminar_proyecto", "Puede eliminar proyecto"),
                    ("pdf_proyecto", "Puede generar pdf de proyecto"),
                ],
            },
        ),
        migrations.CreateModel(
            name="Receptor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_by",
                    models.CharField(max_length=6, verbose_name="Creado por"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado el"),
                ),
                (
                    "updated_by",
                    models.CharField(max_length=6, verbose_name="Actualizado por"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Actualizado el"),
                ),
                (
                    "deleted_by",
                    models.CharField(
                        blank=True,
                        max_length=6,
                        null=True,
                        verbose_name="Eliminado por",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Eliminado el"
                    ),
                ),
                (
                    "idr",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            django.core.validators.MaxLengthValidator(100),
                            helpers.validForm.UnicodeAlphaSpaceValidator(
                                extra_chars="-"
                            ),
                        ],
                        verbose_name="Identificador Receptor",
                    ),
                ),
                (
                    "partidar",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.UnicodeAlphaSpaceValidator(
                                extra_chars="-"
                            ),
                        ],
                        verbose_name="Partida Contable",
                    ),
                ),
                (
                    "generalr",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinValueValidator(100),
                            django.core.validators.MinLengthValidator(3),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.PositiveIntegerValidator(),
                        ],
                        verbose_name="General",
                    ),
                ),
                (
                    "espefr",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinValueValidator(100),
                            django.core.validators.MinLengthValidator(3),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.PositiveIntegerValidator(),
                        ],
                        verbose_name="Específicaciones",
                    ),
                ),
                (
                    "subespefr",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinValueValidator(100),
                            django.core.validators.MinLengthValidator(3),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.PositiveIntegerValidator(),
                        ],
                        verbose_name="Sub-Especialidad",
                    ),
                ),
                (
                    "denomr",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.TextValidator(),
                        ],
                        verbose_name="Denomincación",
                    ),
                ),
                (
                    "presuacorr",
                    models.CharField(
                        max_length=64, verbose_name="Presupuesto acordado"
                    ),
                ),
                (
                    "caufechar",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.TextValidator(),
                        ],
                        verbose_name="Causado a la fecha",
                    ),
                ),
                (
                    "dispr",
                    models.CharField(max_length=64, verbose_name="Disponible a causar"),
                ),
                (
                    "montocr",
                    models.CharField(max_length=64, verbose_name="Monto a ceder"),
                ),
                (
                    "saldofr",
                    models.CharField(max_length=64, verbose_name="Saldo final"),
                ),
                (
                    "direccionr",
                    models.CharField(
                        max_length=64,
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            django.core.validators.MaxLengthValidator(64),
                            helpers.validForm.TextValidator(),
                        ],
                        verbose_name="Dirección cedente",
                    ),
                ),
            ],
            options={
                "verbose_name": "Receptor",
                "verbose_name_plural": "Receptores",
                "permissions": [
                    ("listar_receptor", "Puede listar receptor"),
                    ("agregar_receptor", "Puede agregar receptor"),
                    ("ver_receptor", "Puede ver receptor"),
                    ("editar_receptor", "Puede actualizar receptor"),
                    ("eliminar_receptor", "Puede eliminar receptor"),
                    ("pdf_receptor", "Puede generar pdf de receptor"),
                ],
            },
        ),
    ]
