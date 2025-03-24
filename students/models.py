from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    name = models.CharField(max_length=30)
    addres = models.CharField(max_length=15)
    age = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.pk and Student.objects.filter(user=self.user).exists():
            raise ValueError("This user already has a student profile.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name