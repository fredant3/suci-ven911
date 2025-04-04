# Generated by Django 5.1.1 on 2025-04-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=50)),
                ('device_type', models.CharField(max_length=50)),
                ('device_name', models.CharField(max_length=100)),
                ('operating_system', models.CharField(max_length=100)),
                ('browser', models.CharField(max_length=100)),
                ('method', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
