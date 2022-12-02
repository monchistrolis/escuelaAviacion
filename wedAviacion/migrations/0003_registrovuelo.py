# Generated by Django 4.1.3 on 2022-12-01 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedAviacion', '0002_registro'),
    ]

    operations = [
        migrations.CreateModel(
            name='registroVuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('piloto', models.CharField(max_length=50)),
                ('instructor', models.CharField(max_length=50)),
                ('etapaCurso', models.CharField(max_length=50)),
                ('vueloSolo', models.CharField(max_length=50)),
                ('origen', models.CharField(max_length=50)),
                ('destino', models.CharField(max_length=50)),
                ('horometro_ini', models.FloatField()),
                ('horometro_fin', models.FloatField()),
                ('tacometro_ini', models.FloatField()),
                ('tacometro_fin', models.FloatField()),
                ('combus_ini', models.IntegerField()),
                ('combus_fin', models.IntegerField()),
            ],
        ),
    ]