from django.db import models

from .EquipmentEntity import EquipmentEntity


class EquipmentLoanEntity(models.Model):
    equipments = models.ForeignKey(EquipmentEntity, verbose_name="Equipo ID", on_delete=models.CASCADE)
    department = models.CharField(max_length=100, verbose_name="Departamento")
    loan_date = models.DateField(verbose_name="Fecha del préstamo")
    return_date = models.DateField(verbose_name="Fecha de devolución", null=True, blank=True)

    def __str__(self):
        return f"Loan of {self.equipments.name} to {self.department}"

    class Meta:
        db_table = "gc_equipments_loans"
        verbose_name = "Equipo prestado"
        verbose_name_plural = "Equipos prestados"
        ordering = ["equipments"]
