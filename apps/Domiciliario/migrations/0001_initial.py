# Generated by Django 3.1.2 on 2020-11-08 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domiciliario',
            fields=[
                ('ID_Domiciliario', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=45)),
                ('Apellido', models.CharField(max_length=45)),
                ('Placa_Vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehiculo.vehiculo')),
            ],
        ),
    ]
