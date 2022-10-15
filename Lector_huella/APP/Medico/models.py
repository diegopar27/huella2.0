from django.db import models

# Create your models here.


class medico(models.Model):
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Cc = models.CharField(unique=True, max_length=11,)
    Phone = models.CharField(max_length=13)
    Direction = models.CharField(max_length=50)
    gender = models.CharField(max_length=15)
    Professional_card = models.CharField(max_length=30)
    Specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.Name