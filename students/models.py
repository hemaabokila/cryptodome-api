from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    name = models.CharField(max_length=30)
    addres = models.CharField(max_length=15)
    age = models.IntegerField(max_length=2)

    def __str__(self):
        return self.name