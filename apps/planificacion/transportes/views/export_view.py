from io import BytesIO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from planificacion.transportes.models import Transporte


class TransporteExcelView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "transportes.listar_transporte"

    def get(self, request, *args, **kwargs):
        # Obtener todos los transportes con los campos necesarios
        transportes = Transporte.objects.all().values(
            "estado",
            "mes",
            "transporte",
            "cantidad",
            "created_at",
        )

        # Crear el libro de Excel
        wb = Workbook()
        ws = wb.active

        # Configurar el título del reporte
        ws.merge_cells("A1:E1")
        ws["A1"] = "Reporte de Transportes"
        ws["A1"].alignment = Alignment(horizontal="center")
        ws["A1"].font = Font(bold=True, color="0000FF")
        ws.append([])  # Espacio en blanco

        # Encabezados de columnas
        ws.append(
            [
                "Estado",
                "Mes",
                "Tipo de Transporte",
                "Cantidad",
                "Fecha Creación",
            ]
        )

        # Configurar anchos de columnas
        column_widths = {
            "A": 15,  # Estado
            "B": 15,  # Mes
            "C": 30,  # Tipo de Transporte
            "D": 15,  # Cantidad
            "E": 15,  # Fecha Creación
        }

        for col, width in column_widths.items():
            ws.column_dimensions[col].width = width

        # Llenar con datos
        for transporte in transportes:
            ws.append(
                [
                    transporte["estado"],
                    transporte["mes"],
                    transporte["transporte"],
                    transporte["cantidad"],
                    (
                        transporte["created_at"].strftime("%Y-%m-%d")
                        if transporte["created_at"]
                        else ""
                    ),
                ]
            )

        # Preparar la respuesta
        output = BytesIO()
        wb.save(output)
        output.seek(0)

        return FileResponse(
            output,
            as_attachment=True,
            filename="Transportes.xlsx",
        )
