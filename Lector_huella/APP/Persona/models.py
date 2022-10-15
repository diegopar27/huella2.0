from django.db import models

# Create your models here.


class persona(models.Model):
    Photo = models.ImageField(upload_to='imagenes')
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Cc = models.CharField(unique=True, max_length=11,)
    Phone = models.CharField(max_length=13)
    Direction = models.CharField(max_length=50)
    gender = models.CharField(max_length=4)
    Eps = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date_of_birth = models.DateField()
    meets_the_profile = models.BooleanField()

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Empleados'