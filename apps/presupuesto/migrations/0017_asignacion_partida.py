# Generated by Django 5.1.1 on 2025-05-29 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0016_alter_accion_monto_alter_asignacion_presupuesto'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacion',
            name='partida',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='presupuesto.partida'),
        ),
    ]
