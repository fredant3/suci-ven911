# Generated by Django 5.1.1 on 2025-01-25 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=6, verbose_name='Creado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_by', models.CharField(max_length=6, verbose_name='Actualizado por')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('deleted_by', models.CharField(blank=True, max_length=6, null=True, verbose_name='Eliminado por')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Eliminado el')),
                ('nombre_apellido', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nombre completo')),
            ],
            options={
                'verbose_name': 'Unidad de repuesta inmediata',
                'verbose_name_plural': 'Unidades de repuestas inmediatas',
            },
        ),
    ]
