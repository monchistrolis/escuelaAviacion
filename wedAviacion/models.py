from django.db import models

# Create your models here.
class login(models.Model):
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class registro(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

class registroVuelo(models.Model):
    matricula=models.CharField(max_length=100)
    fecha=models.DateField()
    piloto=models.CharField(max_length=50)
    instructor=models.CharField(max_length=50)
    etapaCurso=models.CharField(max_length=50)
    vueloSolo=models.CharField(max_length=50)
    origen=models.CharField(max_length=50)
    destino=models.CharField(max_length=50)
    horometro_ini=models.FloatField()
    horometro_fin=models.FloatField()
    tacometro_ini=models.FloatField()
    tacometro_fin=models.FloatField()
    combus_ini=models.IntegerField()
    combus_fin=models.IntegerField()
    observacion=models.CharField(max_length=200)

