from django.db import models
from django.contrib import admin

class Brand(models.Model):
	car_brand = models.CharField(max_length = 16)

	def __str__(self):
		return self.car_brand
	
class CarModel(models.Model):
	model = models.CharField(max_length = 32)
	car = models.ForeignKey(Brand)

	def __str__(self):
		return '%s %s' % (self.car.car_brand, self.model)

class CarModelAdmin(admin.ModelAdmin):
	list_display = ('car', 'model')	