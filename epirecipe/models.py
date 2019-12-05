from django.db import models
from django.contrib.auth.models import User
import datetime as dt


class Food(models.Model):
	name = models.CharField(max_length=100)
	dish_image = models.ImageField(upload_to='images/', default='image.jpg')
	ingredients = models.TextField(max_length=1000)
	procedure = models.TextField(max_length=2000)
	 
	def __str__(self):
		return self.name

	def save_food(self):
		self.save()

	def delete_food(self):
		self.delete()