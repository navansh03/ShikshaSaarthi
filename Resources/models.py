from django.db import models

class Course(models.Model):
    name=models.CharField(max_length=30, null =False)
    description= models.CharField(max_length=200,null=True)
    active=models.BooleanField(default=False)
    

