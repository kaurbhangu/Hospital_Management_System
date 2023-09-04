from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name=models.CharField(max_length=40)
    Last_name=models.CharField(max_length=40)
    age=models.IntegerField()
    email=models.EmailField(max_length=255)
    disease=models.CharField(max_length=2000)

    def __str__(self):
       return f'Patient Name:{self.first_name} {self.Last_name}, Age:{self.age}'

