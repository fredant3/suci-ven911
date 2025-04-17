# asignaciones/views/export_view.py
from io import BytesIO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.views.generic import TemplateView
from django.db.models import Q
from helpers.CheckPermisosMixin import CheckPermisosMixin
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from datetime import date
from presupuesto.asignacion.models import Asignacion


class AsignacionExcelView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "asignaciones.listar_asignar_presupuesto"

    def get(self, request, *args, **kwargs):
        # Get search parameter from request
        search_term = request.GET.get("search", "")

        # Base queryset
        asignaciones = Asignacion.objects.all()

        # Apply search filter if term exists
        if search_term:
            asignaciones = asignaciones.filter(
                Q(departamento__icontains=search_term)
                | Q(presupuesto__icontains=search_term)
                | Q(objetivo__icontains=search_term)
                | Q(numero_partida__icontains=search_term)
            )

        # Prepare data for export
        data = asignaciones.values(
            "departamento", "presupuesto", "objetivo", "numero_partida", "created_at"
        )

        # Create Excel workbook
        wb = Workbook()
        ws = wb.active
        ws.title = "Asignaciones Presupuestarias"

        # Title and headers
        ws.merge_cells("A1:E1")
        title_cell = ws["A1"]
        title_cell.value = f"Reporte de Asignaciones Presupuestarias - {date.today().strftime('%Y-%m-%d')}"
        title_cell.font = Font(bold=True, size=14)
        title_cell.alignment = Alignment(horizontal="center")

        headers = [
            "Departamento/Dirección",
            "Presupuesto Asignado",
            "Objetivo General Anual",
            "Número de Partida",
            "Fecha de Creación",
        ]
        ws.append(headers)

        # Set column widths
        column_widths = {
            "A": 30,  # Departamento
            "B": 20,  # Presupuesto
            "C": 40,  # Objetivo
            "D": 20,  # Número de Partida
            "E": 15,  # Fecha Creación
        }

        for col, width in column_widths.items():
            ws.column_dimensions[col].width = width

        # Format header row
        for cell in ws[2]:  # Row 2 contains headers
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal="center")

        # Add data rows
        for asignacion in data:
            ws.append(
                [
                    asignacion["departamento"],
                    asignacion["presupuesto"],
                    asignacion["objetivo"],
                    asignacion["numero_partida"],
                    (
                        asignacion["created_at"].strftime("%Y-%m-%d")
                        if asignacion["created_at"]
                        else ""
                    ),
                ]
            )

        # Prepare response
        output = BytesIO()
        wb.save(output)
        output.seek(0)

        return FileResponse(
            output,
            as_attachment=True,
            filename=f"Asignaciones_Presupuestarias_{date.today().strftime('%Y%m%d')}.xlsx",
        )
