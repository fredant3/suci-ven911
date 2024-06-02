from django.db import models


class SocialMediaAccount(models.Model):
    PLATFORM_CHOICES = [
        ("Facebook", "Facebook"),
        ("Instagram", "Instagram"),
        ("Twitter", "Twitter"),
    ]

    platform = models.CharField(max_length=50, verbose_name='Plataforma', choices=PLATFORM_CHOICES)
    username = models.CharField(max_length=60, verbose_name='Nombre de usuario')
    url = models.URLField(verbose_name='Direccion web')
    followers = models.PositiveSmallIntegerField("Seguidores")
    responsible = models.CharField(max_length=100, verbose_name='Quien administra la red')
    publications = models.PositiveSmallIntegerField("Publicaciones")

    def __str__(self):
        return f"{self.platform} - {self.username}"


class SocialMediaPost(models.Model):
    POST_TYPE_CHOICES = [
        ("reel", "Reel"),
        ("post", "Post"),
        ("story", "Story"),
        ("picture", "Picture"),
    ]

    STATUS_CHOICES = [
        ("published", "Published"), # Publicado
        ("scheduled", "Scheduled"), # Programado
        ("draft", "Draft"), # Borrador
    ]

    account = models.ForeignKey(SocialMediaAccount, verbose_name='Cuenta', on_delete=models.CASCADE)
    post_type = models.CharField(max_length=50, verbose_name='Tipo de publicacion', choices=POST_TYPE_CHOICES)
    content = models.TextField(verbose_name='Contenido')
    publish_date = models.DateField(verbose_name='Fecha de publicacion')
    status = models.CharField(max_length=50, verbose_name='Estatus', choices=STATUS_CHOICES)
    reach = models.IntegerField(verbose_name='Alcance de la publicación')

    def __str__(self):
        return f"{self.post_type} - {self.status}"


class SocialActivity(models.Model):
    ACTIVITY_TYPE_CHOICES = [
        ("workshop", "Workshop"), # Taller
        ("conference", "Conference"), # Conferencia
        ("campaign", "Campaign"), # Campaña
    ]

    activity_type = models.CharField(max_length=50, verbose_name='Tipo de actividad', choices=ACTIVITY_TYPE_CHOICES)
    date = models.DateField(verbose_name='Fecha de la actividad')
    location = models.CharField(max_length=255, verbose_name='Lugar de la actividad')
    description = models.TextField(verbose_name='Descripcion de la actividad')
    reason = models.TextField(verbose_name='Motivo para realizar la actividad')
    beneficiaries = models.IntegerField(verbose_name='Cantidad de personas beneficiadas')

    def __str__(self):
        return f"{self.activity_type} on {self.date}"


class Equipment(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"), # Disponible
        ("loaned", "Loaned"), # Prestado
        ("maintenance", "Maintenance"), # Mantenimiento
    ]

    name = models.CharField(max_length=100, verbose_name='Equipo')
    description = models.TextField(verbose_name='Descripción del equipo')
    status = models.CharField(max_length=50, verbose_name='Estatus del equipo', choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


class EquipmentLoan(models.Model):
    equipment = models.ForeignKey(Equipment, verbose_name='Equipo ID', on_delete=models.CASCADE)
    department = models.CharField(max_length=100, verbose_name='Departamento')
    loan_date = models.DateField(verbose_name='Fecha del préstamo')
    return_date = models.DateField(verbose_name='Fecha de devolución', null=True, blank=True)

    def __str__(self):
        return f"Loan of {self.equipment.name} to {self.department}"
