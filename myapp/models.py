from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    name=models.CharField(max_length=30,null=True)
    age=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    