from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError
from APP.Persona.models import persona


class enfermera(models.Model):
    datos = models.ForeignKey(persona, on_delete=models.CASCADE)
    Professional_card = models.CharField(max_length=30,unique=True)
    Specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.datos.Name
    class Meta:
        verbose_name = 'Enfermera'
