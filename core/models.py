from django.db import models

# Create your models here.

class Usuario (models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    edad = models.IntegerField(verbose_name="Edad")
    mail = models.EmailField(max_length=150, verbose_name="E-mail")
    celular = models.IntegerField(verbose_name="Celular", default=0)
