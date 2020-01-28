from django.db import models

# Create your models here.
class Listings(models.Model):
	title       = models.CharField(max_length=200) #max_length=required intiger
	description = models.TextField()
	price       = models.TextField()
	summary     = models.TextField(default='this is cool!')


	