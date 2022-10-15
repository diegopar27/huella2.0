from django.db import models

# Create your models here.


class historia(models.Model):
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Cc = models.CharField(unique=True, max_length=11,)
    Phone = models.CharField(max_length=13)
    Direction = models.CharField(max_length=50)
    gender = models.CharField(max_length=4)
    Eps = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    Occupation = models.CharField(max_length=100)
    hour_entry_finish = models.DateTimeField(max_length=100)
    Doctor_concept = models.TextField(max_length=1000)

    def __str__(self):
        return self.Name


