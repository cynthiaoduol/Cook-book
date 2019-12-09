from django.db import models
from django.contrib.auth.models import User
import datetime as dt

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')

    def __str__(self):
        return f'{self.user.username} profile'
    
    
    def save_profile(self):
        self.save

    def delete_profile(self):
        self.delete


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

    
class Comment(models.Model):
    comment = models.TextField(max_length=100)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='comment_owner')
    recipe = models.ForeignKey('Food', on_delete=models.CASCADE, related_name='mycomment')

    # def __str__(self):
    #     return f'{self.user.username} comment'

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
    


