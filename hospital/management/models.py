from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.
class User(AbstractUser):
    type_user=models.CharField(max_length=15)


class hospital(models.Model):

    hospital_name=models.CharField(max_length=25)
    admin_name=models.CharField(max_length=50)
    hospital_address=models.TextField()
    # host_email=models.CharField(max_length=40)
    # host_phone=models.CharField(max_length=15)
    # host_pass=models.CharField(max_length=20)
    def __str__(self):
       return self.hospital_name 
class patient(models.Model):

    patient_name=models.CharField(max_length=25)
    status=models.CharField(max_length=50)
    illness=models.TextField()
    doctor_select=models.TextField(default='Vivek')
    # host_email=models.CharField(max_length=40)
    # host_phone=models.CharField(max_length=15)
    # host_pass=models.CharField(max_length=20)
    def __str__(self):
       return self.patient_name 
class doctor(models.Model):

    doctor_name=models.CharField(max_length=25)
    qualification=models.CharField(max_length=50)
    hospital_name=models.TextField()
    # host_email=models.CharField(max_length=40)
    # host_phone=models.CharField(max_length=15)
    # host_pass=models.CharField(max_length=20)
    def __str__(self):
       return self.doctor_name 
class comment(models.Model):
    user_name=models.CharField(max_length=25)
    # qualification=models.CharField(max_length=50)
    comment=models.TextField()
    # host_email=models.CharField(max_length=40)
    # host_phone=models.CharField(max_length=15)
    # host_pass=models.CharField(max_length=20)
    def __str__(self):
       return self.user_name 

class billing(models.Model):
    patient_name=models.CharField(max_length=25)
    hos_name=models.CharField(max_length=50)
    cost=models.IntegerField(null=True,blank=True)  
    paid_cost=models.BooleanField(default=False)
    def __str__(self):
       return self.patient_name 

