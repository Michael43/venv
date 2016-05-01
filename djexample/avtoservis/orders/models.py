from django.db import models
from django.contrib import admin
from user.models import *

class Order(models.Model):
	date = models.DateTimeField('Дата запроса')
	service = models.TextField('Услуга')
	user = models.ForeignKey(UserInform)

	def __str__(self):
		return self.service

class OrderAdmin(admin.ModelAdmin):
	list_display = ('user', 'service', 'date')
	list_filter = ['date']
	search_fields = ['user']