# Generated by Django 5.0.6 on 2024-07-07 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_contrato_rut'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='cantidad_alumnos',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='contrato',
            name='monto_total',
            field=models.IntegerField(default=0),
        ),
    ]
