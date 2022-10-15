from django.db import models

# Create your models here.


class Paciente(models.Model):
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    Cc = models.CharField(unique=True, max_length=11, )
    Phone = models.CharField(max_length=13)
    Direction = models.CharField(max_length=50)
    gender = models.CharField(max_length=4)
    Eps = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date_of_birth = models.DateTimeField()

    def __str__(self):
        return self.Name
