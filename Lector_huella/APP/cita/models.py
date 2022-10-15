from django.db import models

# Create your models here.
from APP.Enfermera.models import enfermera
from APP.Medico.models import medico
from APP.Usuario.models import Paciente


class Cita(models.Model):
    date_and_time = models.DateTimeField()
    doctors = models.ForeignKey(medico, on_delete=models.CASCADE)
    patient = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    eps = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)

    def __str__(self):
        return self.patient.Name