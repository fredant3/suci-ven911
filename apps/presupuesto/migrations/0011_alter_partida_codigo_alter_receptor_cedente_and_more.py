# Generated by Django 5.1.1 on 2025-05-24 20:02

import django.core.validators
import django.db.models.deletion
import helpers.validForm
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0010_alter_receptor_cedente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='codigo',
            field=models.CharField(max_length=64, validators=[django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(64), helpers.validForm.TextValidator()], verbose_name='Código:'),
        ),
        migrations.AlterField(
            model_name='receptor',
            name='cedente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='presupuesto.cedente'),
        ),
        migrations.AlterField(
            model_name='receptor',
            name='partida',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='presupuesto.partida'),
        ),
    ]
