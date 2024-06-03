from django.db import models


class Equipment(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),  # Disponible
        ("loaned", "Loaned"),  # Prestado
        ("maintenance", "Maintenance"),  # Mantenimiento
    ]

    name = models.CharField(max_length=100, verbose_name="Equipo")
    description = models.TextField(verbose_name="Descripción del equipo")
    status = models.CharField(
        max_length=50, verbose_name="Estatus del equipo", choices=STATUS_CHOICES
    )

    def __str__(self):
        return self.name


class EquipmentLoan(models.Model):
    equipment = models.ForeignKey(
        Equipment, verbose_name="Equipo ID", on_delete=models.CASCADE
    )
    department = models.CharField(max_length=100, verbose_name="Departamento")
    loan_date = models.DateField(verbose_name="Fecha del préstamo")
    return_date = models.DateField(
        verbose_name="Fecha de devolución", null=True, blank=True
    )

    def __str__(self):
        return f"Loan of {self.equipment.name} to {self.department}"
