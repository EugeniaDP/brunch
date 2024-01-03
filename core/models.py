from django.db import models

# Create your models here.

class Usuario (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    mail = models.EmailField(max_length=50)
    celular = models.IntegerField(max_length=10)
