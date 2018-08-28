from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EventsBanners(models.Model):
	name = models.CharField(max_length=260,unique=True)
	event_banner = models.ImageField(upload_to='banners')

	def __str__(self):
		return self.name

