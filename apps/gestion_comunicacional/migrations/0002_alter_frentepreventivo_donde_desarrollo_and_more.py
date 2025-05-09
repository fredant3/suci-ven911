# Generated by Django 5.1.1 on 2025-05-10 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_comunicacional', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frentepreventivo',
            name='donde_desarrollo',
            field=models.CharField(choices=[('Es', 'Escuela'), ('Pla', 'Plaza'), ('C', 'Calles'), ('Av', 'Avenida')], max_length=4, verbose_name='Donde se Desarrolló'),
        ),
        migrations.AlterField(
            model_name='frentepreventivo',
            name='tipo_actividad',
            field=models.CharField(choices=[('Ed', 'Educativo'), ('D', 'Deportivo'), ('R', 'Recreativo'), ('C', 'Cultural'), ('A', 'Alimentación'), ('Sa', 'Salud'), ('AJS', 'Asesoria juridica y social'), ('Cur', 'Curso'), ('ta', 'Taller')], max_length=3, verbose_name='Tipo de Actividad'),
        ),
    ]
