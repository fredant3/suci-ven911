# Generated by Django 5.1.1 on 2025-05-29 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0017_asignacion_partida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignacion',
            name='numero_partida',
        ),
    ]
