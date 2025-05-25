from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from typing import Literal
from asesoria.denuncias.models import Denuncia
from asesoria.filmicos.models import RegistroFilmico


class CheckPermisosMixin(object):
    permission_required = ""
    url_redirect = None

    def get_perms(self):
        if isinstance(self.permission_required, str):
            return [self.permission_required]
        else:
            return self.permission_required

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy("auth:login")
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        perms = self.get_perms()

        if any(request.user.has_perm(perm) for perm in perms):
            return super().dispatch(request, *args, **kwargs)

        messages.error(request, "No tienes permisos para realizar esta acción.")
        return redirect(self.get_url_redirect())


AppNames = Literal[
    "asesoria",
    "gestion_humana",
    "administracion",
    "uri",
    "potencia",
    "presupuesto",
    "planificacion",
    "seguridad",
    "gestion_comunicacional",
    "operaciones",
]


class Permisos:
    PERMISSIONS_ASESORIA = (
        Denuncia.PERMISSIONS_ASESORIA_DENUNCIA_AGREGAR,
        Denuncia.PERMISSIONS_ASESORIA_DENUNCIA_EDITAR,
        Denuncia.PERMISSIONS_ASESORIA_DENUNCIA_ELIMINAR,
        Denuncia.PERMISSIONS_ASESORIA_DENUNCIA_EXEL,
        Denuncia.PERMISSIONS_ASESORIA_DENUNCIA_LISTAR,
        Denuncia.PERMISSIONS_ASESORIA_DENUNCIA_VER,
        RegistroFilmico.PERMISSIONS_ASESORIA_REGISTRO_FILMICO_AGREGAR,
        RegistroFilmico.PERMISSIONS_ASESORIA_REGISTRO_FILMICO_EDITAR,
        RegistroFilmico.PERMISSIONS_ASESORIA_REGISTRO_FILMICO_ELIMINAR,
        RegistroFilmico.PERMISSIONS_ASESORIA_REGISTRO_FILMICO_EXEL,
        RegistroFilmico.PERMISSIONS_ASESORIA_REGISTRO_FILMICO_LISTAR,
        RegistroFilmico.PERMISSIONS_ASESORIA_REGISTRO_FILMICO_VER,
    )

    PERMISSIONS_GESTION_HUMANA = (
        # CARGO
        "rrhh.agregar_cargo",
        "rrhh.editar_cargo",
        "rrhh.eliminar_cargo",
        "rrhh.exel_cargo",
        "rrhh.listar_cargo",
        "rrhh.ver_cargo",
        # CONTRATO
        "rrhh.agregar_contrato",
        "rrhh.editar_contrato",
        "rrhh.eliminar_contrato",
        "rrhh.exel_contrato",
        "rrhh.listar_contrato",
        "rrhh.ver_contrato",
        # DOTACION
        "rrhh.agregar_dotacion",
        "rrhh.editar_dotacion",
        "rrhh.eliminar_dotacion",
        "rrhh.exel_dotacion",
        "rrhh.listar_dotacion",
        "rrhh.ver_dotacion",
        # EDUCACION
        "rrhh.agregar_educacion",
        "rrhh.editar_educacion",
        "rrhh.eliminar_educacion",
        "rrhh.exel_educacion",
        "rrhh.listar_educacion",
        "rrhh.ver_educacion",
        # EMPLEAD
        "rrhh.agregar_empleado",
        "rrhh.editar_empleado",
        "rrhh.eliminar_empleado",
        "rrhh.exel_empleado",
        "rrhh.listar_empleado",
        "rrhh.ver_empleado",
        # FAMILIARES
        "rrhh.agregar_familiar",
        "rrhh.eliminar_familiar",
        "rrhh.exel_familiar",
        "rrhh.listar_familiares",
        "rrhh.modificar_familiar",
        "rrhh.ver_familiar",
        # TIPO_SUELDO
        "rrhh.agregar_tipo_sueldo",
        "rrhh.eliminar_tipo_sueldo",
        "rrhh.exel_tipo_sueldo",
        "rrhh.listar_tipo_sueldos",
        "rrhh.modificar_tipo_sueldo",
        "rrhh.ver_tipo_sueldo",
        # SUELDO
        "rrhh.agregar_sueldo",
        "rrhh.eliminar_sueldo",
        "rrhh.exel_sueldo",
        "rrhh.listar_sueldos",
        "rrhh.modificar_sueldo",
        "rrhh.ver_sueldo",
    )

    PERMISSIONS_ADMINISTRACION = (
        # TIPO_ARTICULO
        "administracion.agregar_tipo_articulo",
        "administracion.editar_tipo_articulo",
        "administracion.eliminar_tipo_articulo",
        "administracion.listar_tipo_articulo",
        "administracion.ver_tipo_articulo",
        # ARTICULO
        "administracion.agregar_articulo",
        "administracion.editar_articulo",
        "administracion.eliminar_articulo",
        "administracion.listar_articulo",
        "administracion.ver_articulo",
        # ASIGNACION
        "administracion.agregar_asignacion",
        "administracion.editar_asignacion",
        "administracion.eliminar_asignacion",
        "administracion.listar_asignacion",
        "administracion.ver_asignacion",
        # TIPO_AVERIA
        "administracion.agregar_tipo_averia",
        "administracion.editar_tipo_averia",
        "administracion.eliminar_tipo_averia",
        "administracion.listar_tipo_averia",
        "administracion.ver_tipo_averia",
        # AVERIA
        "administracion.agregar_averia",
        "administracion.editar_averia",
        "administracion.eliminar_averia",
        "administracion.listar_averia",
        "administracion.ver_averia",
        # COMPRA
        "administracion.agregar_compra",
        "administracion.editar_compra",
        "administracion.eliminar_compra",
        "administracion.listar_compra",
        "administracion.ver_compra",
        # DEPARTAMENTO
        "administracion.agregar_departamento",
        "administracion.editar_departamento",
        "administracion.eliminar_departamento",
        "administracion.listar_departamento",
        "administracion.ver_departamento",
        # SEDE
        "administracion.agregar_sede",
        "administracion.editar_sede",
        "administracion.eliminar_sede",
        "administracion.listar_sede",
        "administracion.ver_sede",
    )

    PERMISSIONS_URI = (
        "potencia.agregar_uri",
        "potencia.editar_uri",
        "potencia.eliminar_uri",
        "potencia.listar_uri",
        "potencia.ver_uri",
    )

    PERMISSIONS_POTENCIA = (
        # TIPO_INCIDENCIA
        "potencia.agregar_tipo_incidencia",
        "potencia.editar_tipo_incidencia",
        "potencia.eliminar_tipo_incidencia",
        "potencia.listar_tipo_incidencia",
        "potencia.ver_tipo_incidencia",
        # INCIDENCIA
        "potencia.agregar_incidencia",
        "potencia.editar_incidencia",
        "potencia.eliminar_incidencia",
        "potencia.listar_incidencia",
        "potencia.ver_incidencia",
    )

    PERMISSIONS_PRESUPUESTO = (
        # ACCION
        "presupuesto.agregar_accion",
        "presupuesto.editar_accion",
        "presupuesto.eliminar_accion",
        "presupuesto.listar_accion",
        "presupuesto.pdf_accion",
        "presupuesto.ver_accion",
        # ASIGNAR_PRESUPUESTO
        "presupuesto.agregar_asignar_presupuesto",
        "presupuesto.editar_asignar_presupuesto",
        "presupuesto.eliminar_asignar_presupuesto",
        "presupuesto.listar_asignar_presupuesto",
        "presupuesto.pdf_asignar_presupuesto",
        "presupuesto.ver_asignar_presupuesto",
        # CEDENTE
        "presupuesto.agregar_cedente",
        "presupuesto.editar_cedente",
        "presupuesto.eliminar_cedente",
        "presupuesto.listar_cedente",
        "presupuesto.pdf_cedente",
        "presupuesto.ver_cedente",
        # PROYECTO
        "presupuesto.agregar_proyecto",
        "presupuesto.editar_proyecto",
        "presupuesto.eliminar_proyecto",
        "presupuesto.listar_proyecto",
        "presupuesto.pdf_proyecto",
        "presupuesto.ver_proyecto",
        # RECEPTOR
        "presupuesto.agregar_receptor",
        "presupuesto.editar_receptor",
        "presupuesto.eliminar_receptor",
        "presupuesto.listar_receptor",
        "presupuesto.pdf_receptor",
        "presupuesto.ver_receptor",
    )

    PERMISSIONS_PLANIFICACION = (
        # ACTIVIDAD
        "planificacion.agregar_actividad",
        "planificacion.editar_actividad",
        "planificacion.eliminar_actividad",
        "planificacion.listar_actividad",
        "planificacion.ver_actividad",
        # INFRAESTRUCTURA
        "planificacion.agregar_infraestructura",
        "planificacion.editar_infraestructura",
        "planificacion.eliminar_infraestructura",
        "planificacion.listar_infraestructura",
        "planificacion.ver_infraestructura",
        # LLAMADA
        "planificacion.agregar_llamada",
        "planificacion.editar_llamada",
        "planificacion.eliminar_llamada",
        "planificacion.listar_llamada",
        "planificacion.ver_llamada",
        # OBJETIVO
        "planificacion.agregar_objetivo",
        "planificacion.editar_objetivo",
        "planificacion.eliminar_objetivo",
        "planificacion.listar_objetivo",
        "planificacion.ver_objetivo",
        # TRANSPORTE
        "planificacion.agregar_transporte",
        "planificacion.editar_transporte",
        "planificacion.eliminar_transporte",
        "planificacion.listar_transporte",
        "planificacion.ver_transporte",
    )

    PERMISSIONS_SEGURIDAD = (
        # ENTRADA
        "seguridad.agregar_entrada",
        "seguridad.eliminar_entrada",
        "seguridad.listar_entradas",
        "seguridad.modificar_entrada",
        "seguridad.ver_entrada",
        # GESTION
        "seguridad.agregar_gestion",
        "seguridad.eliminar_gestion",
        "seguridad.listar_gestiones",
        "seguridad.modificar_gestion",
        "seguridad.ver_gestion",
        # SALIDA
        "seguridad.agregar_salida",
        "seguridad.eliminar_salida",
        "seguridad.listar_salidas",
        "seguridad.modificar_salida",
        "seguridad.ver_salida",
        # VEHICULO
        "seguridad.agregar_vehiculo",
        "seguridad.eliminar_vehiculo",
        "seguridad.listar_vehiculos",
        "seguridad.modificar_vehiculo",
        "seguridad.ver_vehiculo",
    )

    PERMISSIONS_GESTION_COMUNICACIONAL = (
        # FRENTE_PREVENTIVO
        "gestion_comunicacional.agregar_frentepreventivo",
        "gestion_comunicacional.editar_frentepreventivo",
        "gestion_comunicacional.eliminar_frentepreventivo",
        "gestion_comunicacional.listar_frentepreventivo",
        "gestion_comunicacional.ver_frentepreventivo",
        # GESTION_COMUNICACIONAL
        "gestion_comunicacional.agregar_gestion_comunicacional",
        "gestion_comunicacional.editar_gestion_comunicacional",
        "gestion_comunicacional.eliminar_gestion_comunicacional",
        "gestion_comunicacional.listar_gestion_comunicacional",
        "gestion_comunicacional.ver_gestion_comunicacional",
    )

    PERMISSIONS_OPERACIONES = (
        # ORGANISMO_EMERGENCIA
        "emergencia.agregar_organismo_emergencia",
        "emergencia.editar_organismo_emergencia",
        "emergencia.eliminar_organismo_emergencia",
        "emergencia.listar_organismo_emergencia",
        "emergencia.ver_organismo_emergencia",
        # TIPO_INCIDENCIA_EMERGENCIA
        "emergencia.agregar_tipo_incidencia_emergencia",
        "emergencia.editar_tipo_incidencia_emergencia",
        "emergencia.eliminar_tipo_incidencia_emergencia",
        "emergencia.listar_tipo_incidencia_emergencia",
        "emergencia.ver_tipo_incidencia_emergencia",
        # EMERGENCIA
        "emergencia.agregar_emergencia",
        "emergencia.editar_emergencia",
        "emergencia.eliminar_emergencia",
        "emergencia.listar_emergencia",
        "emergencia.ver_emergencia",
    )

    permisos_apps = {
        "asesoria": PERMISSIONS_ASESORIA,
        "gestion_humana": PERMISSIONS_GESTION_HUMANA,
        "administracion": PERMISSIONS_ADMINISTRACION,
        "uri": PERMISSIONS_URI,
        "potencia": PERMISSIONS_POTENCIA,
        "presupuesto": PERMISSIONS_PRESUPUESTO,
        "planificacion": PERMISSIONS_PLANIFICACION,
        "seguridad": PERMISSIONS_SEGURIDAD,
        "gestion_comunicacional": PERMISSIONS_GESTION_COMUNICACIONAL,
        "operaciones": PERMISSIONS_OPERACIONES,
    }

    @classmethod
    def check_permissions(cls, user: User, app_name: AppNames) -> bool:
        if not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        return any(user.has_perm(perm) for perm in cls.permisos_apps[app_name])
