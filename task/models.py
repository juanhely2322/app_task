from datetime import datetime
from multiprocessing.spawn import import_main_path
from ssl import create_default_context
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class task(models.Model):
    title= models.CharField(max_length=100)
    description=models.TextField(blank=True)# blanck=True en caso de que no envie nada el campo permanecera bacio
    created=models.DateTimeField(auto_now_add=True)
    datecomplete=models.DateTimeField(null=True, blank=True)
    important=models.BooleanField(default=False) 
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #str , self hace referencia a la propia clase
    def __str__(self):
        return self.title +"-by "+ self.user.username+ " created " + self.created.__str__()
        

# Create your models here.
