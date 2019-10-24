from django.db import models
from django.urls import reverse

# Create your models here.

class StudentData(models.Model):
    name = models.CharField(max_length=35)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    course = models.CharField(max_length=20)
    phone = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("result")