from io import BytesIO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.views.generic import TemplateView
from helpers.CheckPermisosMixin import CheckPermisosMixin
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from rrhh.cargos.models import Cargo  # Asegúrate de importar el modelo Cargo


class CargoExcelView(LoginRequiredMixin, CheckPermisosMixin, TemplateView):
    permission_required = "rrhh.cargo.exel_cargo"  # Define el permiso necesario

    def get(self, request, *args, **kwargs):
        cargos = Cargo.objects.all().values("cargo", "estatus")

        # Crea un archivo Excel en memoria
        wb = Workbook()
        ws = wb.active

        # Agrega el título en la primera fila
        ws.merge_cells("A1:B1")  # Mezcla las celdas de A1 a B1
        ws["A1"] = "Listado de Cargos"  # Agrega el texto del título
        ws["A1"].alignment = Alignment(
            horizontal="center"
        )  # Centra el texto del título
        ws["A1"].font = Font(
            bold=True, color="0000FF"
        )  # Establece el texto en negrita y color azul
        ws["A2"] = ""  # Agrega una fila vacía

        # Agrega los encabezados de las columnas
        ws.append(["Cargo", "Estatus"])

        # Ajusta el ancho de las columnas
        columnas = ws.column_dimensions
        columnas["A"].width = 30
        columnas["B"].width = 15

        # Agrega los datos de los cargos
        for cargo in cargos:
            ws.append([cargo["cargo"], cargo["estatus"]])

        # Convierte el archivo Excel en memoria a bytes
        output = BytesIO()
        wb.save(output)
        output.seek(0)

        # Devuelve el archivo Excel como respuesta
        return FileResponse(output, as_attachment=True, filename="Cargos.xlsx")
