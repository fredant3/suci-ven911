# Generated by Django 5.1.1 on 2025-05-10 22:06

import django.core.validators
import django.db.models.deletion
import helpers.validForm
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='apellidos',
            field=models.CharField(blank=True, max_length=90, null=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(90), helpers.validForm.UnicodeAlphaSpaceValidator()], verbose_name='Apellidos del Familiar'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='cedula',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(7), django.core.validators.MaxLengthValidator(14), helpers.validForm.CedulaVenezolanaValidator()], verbose_name='Cédula de Identidad'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='discapacidad',
            field=models.BooleanField(blank=True, choices=[(True, 'si'), (False, 'no')], default=(False, 'no'), null=True, verbose_name='Discapacidad'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='empleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rrhh.empleado', verbose_name='Empleado'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('s', 'Soltero'), ('c', 'Casado'), ('d', 'Divorviado'), ('v', 'Viudo')], max_length=1, null=True, verbose_name='Estado civil'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='nombres',
            field=models.CharField(blank=True, max_length=90, null=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(90), helpers.validForm.UnicodeAlphaSpaceValidator()], verbose_name='Nombres del Familiar'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='parentezco',
            field=models.CharField(blank=True, choices=[('hermano', 'Hermana|Hermano'), ('pareja', 'Conyugue'), ('mama', 'Madre'), ('papa', 'Padre'), ('hijo', 'Hija|Hijo')], max_length=7, null=True, verbose_name='Parentezco'),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='sexo',
            field=models.CharField(blank=True, choices=[('f', 'Femenino'), ('m', 'Masculino')], max_length=1, null=True, verbose_name='Género'),
        ),
    ]
