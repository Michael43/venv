from django.db import models
from django.contrib import admin
from car.models import *

class UserInform(models.Model):
	user = models.CharField(max_length = 32)
	vin = models.CharField(max_length = 16)
	number = models.CharField(max_length = 8)
	phone_number = models.IntegerField()
	car = models.ForeignKey('car.CarModel')
	
	def __str__(self):
		return self.user

class UserAdmin(admin.ModelAdmin):
	list_display = ('user', 'vin', 'number','car','phone_number')	
	search_fields = ['user','vin','phone_number']	