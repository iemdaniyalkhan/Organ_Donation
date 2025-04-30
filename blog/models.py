from asyncio.windows_events import NULL
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os

class Post(models.Model):
	title = models.CharField(default="abc",max_length=100)
	file = models.FileField(null=True,blank=True,upload_to='Files')
	content = models.TextField()
	date_posted = models.CharField(default="abc",max_length=100)
	author = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
	
	class Meta:
		db_table = 'Post'

	def __str__(self):
		return self.title

	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		return extension

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

        
