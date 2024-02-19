from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_admin1=models.BooleanField(default=False)

class Student(models.Model):
    user_1=models.ForeignKey(Login,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=10)
    image=models.FileField(upload_to='images/')
    dob=models.DateField()

class Admin1(models.Model):
    user_2 = models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number = models.CharField(max_length=10)