from django.db import models
import django.db.models.functions.datetime as datetime

# Create your models here.
class createtodo(models.Model):
	Name=models.CharField(max_length=120,default=None)
	Date=models.DateField(default=None,null=False)
	Time=models.TimeField(default=None,null=False)
	Description=models.TextField(blank=False,default=None,max_length=1000)
	History=models.CharField(blank=True,null=True,max_length=200,default=None)
