from io import BytesIO
from administracion.asignaciones.models import Asignacion  # Cambio de modelo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font


class AsignacionExcelView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "administracion.listar_asignacion"  # Permiso actualizado

    def get(self, request, *args, **kwargs):
        asignaciones = Asignacion.objects.all().values(
            "articulo__serial",  # Accede a campos relacionados
            "sede__sede",
            "departamento__nombre",
            "cantidad",
            "descripcion",
            "observaciones",
            "created_at",
        )

        # Crea un archivo Excel en memoria
        wb = Workbook()
        ws = wb.active

        # Título del reporte
        ws.merge_cells("A1:G1")  # Ajustado a 7 columnas
        ws["A1"] = "Reporte de Asignaciones"
        ws["A1"].alignment = Alignment(horizontal="center")
        ws["A1"].font = Font(bold=True, color="0000FF")
        ws.append([])  # Espacio en blanco

        # Encabezados
        ws.append([
            "Artículo",
            "Sede",
            "Departamento",
            "Cantidad",
            "Descripción",
            "Observaciones",
            "Fecha de Creación",
        ])

        # Ajustes de ancho de columnas
        column_widths = {
            'A': 25,  # Artículo
            'B': 20,  # Sede
            'C': 25,  # Departamento
            'D': 12,  # Cantidad
            'E': 40,  # Descripción
            'F': 40,  # Observaciones
            'G': 20,  # Fecha
        }

        for col, width in column_widths.items():
            ws.column_dimensions[col].width = width

        # Datos
        for registro in asignaciones:
            ws.append([
                registro["articulo__serial"],
                registro["sede__sede"],
                registro["departamento__nombre"],
                registro["cantidad"],
                registro["descripcion"],
                registro["observaciones"],
                registro["created_at"].strftime("%Y-%m-%d %H:%M") if registro["created_at"] else ""
            ])

        # Generar respuesta
        output = BytesIO()
        wb.save(output)
        output.seek(0)

        return FileResponse(
            output,
            as_attachment=True,
            filename="Asignaciones.xlsx"  # Nombre actualizado
        )