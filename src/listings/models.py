from django.db import models

# Create your models here.
class Listings(models.Model):
	title       = models.CharField(max_length=200) # max_length=required intiger
	description = models.TextField(blank=True, null=True)
	price       = models.DecimalField(decimal_places=2, max_digits=1000000)
	summary     = models.TextField(blank=False, null=False)
	featured    = models.BooleanField(default=False) #nulle = True, Default = True


	