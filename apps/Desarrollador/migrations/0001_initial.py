# Generated by Django 3.1.2 on 2020-11-08 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desarrollador',
            fields=[
                ('ID_Desarrolador', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=45)),
            ],
        ),
    ]
