from django.db import models

# Create your models here.

class StudentData(models.Model):
    name = models.CharField(max_length=35)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    course = models.CharField(max_length=20)
    phone = models.FloatField()