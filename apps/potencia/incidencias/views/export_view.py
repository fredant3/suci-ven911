from io import BytesIO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, Border, Side
from administracion.sedes.models import Sede
from administracion.departamentos.models import Departamento
from potencia.tipo_incidencia.models import TipoIncidencia
from potencia.incidencias.models import Incidencia, ESTADOS_CHOICES, INCIDENCIA_CHOICES


class IncidenciaExcelView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "incidencia.listar_incidencia"

    def get(self, request, *args, **kwargs):
        # Consulta optimizada con select_related para relaciones
        incidencias = Incidencia.objects.select_related(
            "sede", "departamento", "tipo_incidencia"
        ).values(
            "id",
            "sede__sede",
            "departamento__nombre",
            "tipo_incidencia__tipo",
            "estado",
            "tipo_solicitud",
            "observaciones",
            "created_at",
            "updated_at",
        )

        wb = Workbook()
        ws = wb.active
        ws.title = "Reporte de Incidencias"

        # Configuración del título (ajustado a 9 columnas)
        ws.merge_cells("A1:I1")
        title_cell = ws["A1"]
        title_cell.value = "REGISTRO DE INCIDENCIAS"
        title_cell.alignment = Alignment(horizontal="center")
        title_cell.font = Font(bold=True, size=14, color="0047AB")

        # Encabezados actualizados
        headers = [
            ("ID", 10),
            ("Sede", 25),
            ("Departamento", 25),
            ("Tipo Incidencia", 25),
            ("Estado", 15),
            ("Tipo Solicitud", 20),
            ("Observaciones", 40),
            ("Fecha Creación", 20),
            ("Fecha Actualización", 20),
        ]

        # Configurar columnas
        for col_num, (header, width) in enumerate(headers, 1):
            col_letter = chr(64 + col_num)
            ws.column_dimensions[col_letter].width = width
            cell = ws.cell(row=2, column=col_num, value=header)
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal="center")

        # Mapeo de estados y tipos de solicitud
        estados_map = dict(ESTADOS_CHOICES)
        solicitud_map = dict(INCIDENCIA_CHOICES)

        # Llenar datos
        for row_num, incidencia in enumerate(incidencias, 3):
            ws.append(
                [
                    incidencia["id"],
                    incidencia["sede__nombre"],
                    incidencia["departamento__nombre"],
                    incidencia["tipo_incidencia__nombre"],
                    estados_map.get(incidencia["estado"], "Desconocido"),
                    solicitud_map.get(incidencia["tipo_solicitud"], "Desconocido"),
                    incidencia["observaciones"] or "N/A",
                    (
                        incidencia["created_at"].strftime("%d/%m/%Y %H:%M")
                        if incidencia["created_at"]
                        else "N/A"
                    ),
                    (
                        incidencia["updated_at"].strftime("%d/%m/%Y %H:%M")
                        if incidencia["updated_at"]
                        else "N/A"
                    ),
                ]
            )

        # Aplicar bordes
        border = Border(
            left=Side(style="thin"),
            right=Side(style="thin"),
            top=Side(style="thin"),
            bottom=Side(style="thin"),
        )
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, max_col=len(headers)):
            for cell in row:
                cell.border = border

        # Generar archivo
        output = BytesIO()
        wb.save(output)
        output.seek(0)

        return FileResponse(
            output, as_attachment=True, filename="reporte_incidencias.xlsx"
        )