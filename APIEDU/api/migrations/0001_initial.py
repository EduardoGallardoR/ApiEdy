# Generated by Django 3.2.4 on 2023-11-07 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id_respuesta', models.AutoField(db_column='idrespuesta', primary_key=True, serialize=False)),
                ('colore', models.CharField(db_column='color', max_length=100)),
                ('frecuenciacome', models.CharField(db_column='frecuenciacom', max_length=100)),
                ('alquiladoañoe', models.CharField(db_column='alquilado', max_length=100)),
                ('frecuenciaalquie', models.CharField(db_column='frecuenciaalqui', max_length=100)),
                ('factorese', models.CharField(db_column='factores', max_length=100)),
                ('metodopagoe', models.CharField(db_column='metodopag', max_length=100)),
                ('malexpe', models.CharField(db_column='malexperiencia', max_length=100)),
                ('dispositivoe', models.CharField(db_column='dispositivo', max_length=100)),
                ('recibirofe', models.CharField(db_column='recibiof', max_length=100)),
                ('asistenciae', models.CharField(db_column='asistencia', max_length=100)),
            ],
            options={
                'db_table': 'respuesta',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(db_column='idusu', primary_key=True, serialize=False)),
                ('nombreu', models.CharField(db_column='nombre', max_length=100)),
                ('apellidou', models.CharField(db_column='apellido', max_length=100)),
                ('correou', models.CharField(db_column='correo', max_length=100, unique=True)),
                ('contraseñau', models.CharField(db_column='contraseña', max_length=255)),
            ],
            options={
                'db_table': 'Usuario',
            },
        ),
    ]
