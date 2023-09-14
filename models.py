from django.db import models
from django.contrib.auth.models import User# Create your models here.




class Personal_Information(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    fathername = models.CharField(max_length=30)
    fathercontact  =  models.CharField(max_length=30)
    mothername = models.CharField(max_length=30)
    mothercontact = models.CharField(max_length=30)
    Spousesname = models.CharField(max_length=30)
    caste =  models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    religions = models.CharField(max_length=30)
    maritalstatus = models.CharField(max_length=30)
    professionalreferences= models.CharField(max_length=30)
    image = models.FileField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return "name"



class Job_Information(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    Jobtitle = models.CharField(max_length=30)
    dateofjoining= models.CharField(max_length=30)
    worklocation= models.CharField(max_length=30)
    salary = models.CharField(max_length=30)
    def __str__(self):
        return "Jobtitle"

 
class Employee_Education_Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    examinationpassed = models.CharField(max_length=30)
    institute = models.CharField(max_length=30)
    university = models.CharField(max_length=30)
    yearofpassing = models.CharField(max_length=30)
    grades = models.CharField(max_length=30)
    def __str__(self):
        return "examinationpassed"


class Employee_Old_Service_History(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    organization = models.CharField(max_length=30)
    jobtitle = models.CharField(max_length=30)
    periodofservice = models.CharField(max_length=30)
    compensation = models.CharField(max_length=30)
    reasonforleaving = models.CharField(max_length=30)


class Declaration(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    signature = models.ImageField(upload_to='images/', null=True, blank=True)

    # signature = models.CharField(max_length=30)





