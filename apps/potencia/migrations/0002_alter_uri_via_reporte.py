# Generated by Django 5.1.1 on 2025-05-10 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uri',
            name='via_reporte',
            field=models.CharField(blank=True, choices=[('rs', 'RRSS'), ('rad', 'Radio'), ('casu', 'Casual'), ('Telefónico', 'Telefónico'), ('otr', 'Otro')], max_length=12, null=True, verbose_name='Vía del Reporte'),
        ),
    ]
