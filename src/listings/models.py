from django.db import models

# Create your models here.
class Listings(models.Model):
	title       = models.CharField(max_length=200) # max_length=required intiger
	description = models.TextField(blank=True, null=True)
	price       = models.DecimalField(decimal_places=2, max_digits=1000)
	summary     = models.TextField()


	