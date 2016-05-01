from django.db import models

class SelectCity(models.Model):
	city = models.CharField(max_length = 16)
	def __str__(self):
		return self.city
		
