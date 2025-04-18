# Generated by Django 5.1.1 on 2025-04-17 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_comunicacional', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestioncomunicacional',
            name='actividad_preventiva',
            field=models.CharField(choices=[('I', 'Individual'), ('Fp', 'Frente preventivo')], max_length=2),
        ),
        migrations.AlterField(
            model_name='gestioncomunicacional',
            name='ambito_accion',
            field=models.CharField(choices=[('Ed', 'Educativo'), ('D', 'Deportivo'), ('R', 'Recreativo'), ('C', 'Cultural'), ('A', 'Alimentación'), ('Sa', 'Salud'), ('AJS', 'Asesoria juridica y social')], max_length=3, verbose_name='Ambito de acción'),
        ),
    ]
