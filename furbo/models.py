from django.db import models

# Create your models here.
class Equipos(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.TextField()

    def __str__(self):
        return f"Nombre_ {self.nombre}"
