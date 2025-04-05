from io import BytesIO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from rrhh.contratos.models import Contrato  # Asegúrate de importar el modelo Contrato


class ContratoExcelView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "rrhh.contratos.exel_contrato"  # Define el permiso necesario

    def get(self, request, *args, **kwargs):
        contratos = Contrato.objects.all().values(
            "tipo",
            "comision_servicio",
            "pnb",
            "departamento__nombre",  # Asume que el modelo Departamento tiene un campo 'nombre'
            "cargo__cargo",  # Asume que el modelo Cargo tiene un campo 'cargo'
            "sede__nombre",  # Asume que el modelo Sede tiene un campo 'nombre'
            "fecha_ingreso_911",
            "fecha_ingreso_apn",
            "fasmij",
            "fecha_ingreso",
            "fecha_culminacion",
            "empleado__nombres",  # Asume que el modelo Empleado tiene un campo 'nombres'
            "empleado__apellidos",  # Asume que el modelo Empleado tiene un campo 'apellidos'
        )

        # Crea un archivo Excel en memoria
        wb = Workbook()
        ws = wb.active

        # Agrega el título en la primera fila
        ws.merge_cells("A1:M1")  # Mezcla las celdas de A1 a M1
        ws["A1"] = "Listado de Contratos"  # Agrega el texto del título
        ws["A1"].alignment = Alignment(
            horizontal="center"
        )  # Centra el texto del título
        ws["A1"].font = Font(
            bold=True, color="0000FF"
        )  # Establece el texto en negrita y color azul
        ws["A2"] = ""  # Agrega una fila vacía

        # Agrega los encabezados de las columnas
        ws.append(
            [
                "Tipo de Contrato",
                "Comisión de Servicio",
                "PNB",
                "Departamento",
                "Tipo de Personal",
                "Cargo",
                "Sede",
                "Fecha de Ingreso 911",
                "Fecha de Ingreso APN",
                "FASMIJ",
                "Fecha de Ingreso",
                "Fecha de Culminación",
                "Empleado",
            ]
        )

        # Ajusta el ancho de las columnas
        columnas = ws.column_dimensions
        columnas["A"].width = 20
        columnas["B"].width = 20
        columnas["C"].width = 15
        columnas["D"].width = 20
        columnas["E"].width = 20
        columnas["F"].width = 20
        columnas["G"].width = 20
        columnas["H"].width = 20
        columnas["I"].width = 20
        columnas["J"].width = 15
        columnas["K"].width = 20
        columnas["L"].width = 20
        columnas["M"].width = 30

        # Agrega los datos de los contratos
        for contrato in contratos:
            ws.append(
                [
                    contrato["tipo"],
                    "Sí" if contrato["comision_servicio"] else "No",
                    "Sí" if contrato["pnb"] else "No",
                    contrato["departamento__nombre"],
                    contrato["cargo__cargo"],
                    contrato["sede__nombre"],
                    (
                        contrato["fecha_ingreso_911"].strftime("%Y-%m-%d")
                        if contrato["fecha_ingreso_911"]
                        else ""
                    ),
                    (
                        contrato["fecha_ingreso_apn"].strftime("%Y-%m-%d")
                        if contrato["fecha_ingreso_apn"]
                        else ""
                    ),
                    "Sí" if contrato["fasmij"] else "No",
                    (
                        contrato["fecha_ingreso"].strftime("%Y-%m-%d")
                        if contrato["fecha_ingreso"]
                        else ""
                    ),
                    (
                        contrato["fecha_culminacion"].strftime("%Y-%m-%d")
                        if contrato["fecha_culminacion"]
                        else ""
                    ),
                    f"{contrato['empleado__nombres']} {contrato['empleado__apellidos']}",
                ]
            )

        # Convierte el archivo Excel en memoria a bytes
        output = BytesIO()
        wb.save(output)
        output.seek(0)

        # Devuelve el archivo Excel como respuesta
        return FileResponse(output, as_attachment=True, filename="Contratos.xlsx")
