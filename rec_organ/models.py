from django.db import models
from django.db.models.fields import NullBooleanField
from django.contrib.auth.models import User
from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os







class Admin_details(models.Model):
    
    
        
    
    Username = models.CharField(default="admin",max_length=100)
    
    Password = models.CharField(default="admin",max_length=100)

    class Meta:
        db_table = 'Admin_Details'
    
class user_Details(models.Model):
    Username = models.CharField(default=None,max_length=100)
    Password = models.CharField(default=None,max_length=100)
    Adhar = models.IntegerField(default=None,max_length=100)
    Image1 = models.ImageField(upload_to='Files')
    video = models.ImageField(default=None,upload_to='Files')


    class Meta:
        db_table = 'User_Details'
        
    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class student(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default=None,max_length=100)
    branch = models.CharField(default=None,max_length=100)
    year = models.CharField(default=None,max_length=100)
    sem = models.CharField(default=None,max_length=100)
    internship = models.CharField(default=None,max_length=100)
    project = models.CharField(default=None,max_length=100)
    branch = models.CharField(default=None,max_length=100)


class organ(models.Model):
    donor_name=  models.CharField(default=None,max_length=100)
    donor_age=  models.CharField(default=None,max_length=100)
    donor_BG=  models.CharField(default=None,max_length=100)
    
    
   
    name = models.CharField(default=None,max_length=100)
    location = models.CharField(default=None,max_length=100)
    
    price = models.CharField(default=None,max_length=100)
    stat = models.CharField(default="unbooked",max_length=100)

    class Meta:
        db_table = 'Organ_details'
    

class requests_made(models.Model):
    
    names = models.CharField(default=None,max_length=100)
    thing = models.CharField(default=None,max_length=100)
    status = models.CharField(default=None,max_length=100)
    Image1 = models.ImageField(default=None,upload_to='Files')
    video = models.FileField(null=True,blank=True,upload_to='Files')
    vid_id = models.IntegerField(default=0,max_length=100)

    def extension(self):
        name, extension = os.path.splitext(self.video.name)
        return extension
        
    
        
    class Meta:
        db_table = 'Request_made_Details'



