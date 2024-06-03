from django.db import models


class SocialActivityEntity(models.Model):
    ACTIVITY_TYPE_CHOICES = [
        ("workshop", "Workshop"),  # Taller
        ("conference", "Conference"),  # Conferencia
        ("campaign", "Campaign"),  # Campaña
    ]

    activity_type = models.CharField(
        max_length=50, verbose_name="Tipo de actividad", choices=ACTIVITY_TYPE_CHOICES
    )
    date = models.DateField(verbose_name="Fecha de la actividad")
    location = models.CharField(max_length=255, verbose_name="Lugar de la actividad")
    description = models.TextField(verbose_name="Descripcion de la actividad")
    reason = models.TextField(verbose_name="Motivo para realizar la actividad")
    beneficiaries = models.IntegerField(
        verbose_name="Cantidad de personas beneficiadas"
    )

    def __str__(self):
        return f"{self.activity_type} on {self.date}"
