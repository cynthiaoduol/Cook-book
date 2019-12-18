from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.urls import reverse
from tinymce.models import HTMLField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')


    def save_profile(self):
        self.save

    def delete_profile(self):
        self.delete


class Food(models.Model):
    name = models.CharField(max_length=100)
    dish_image = models.ImageField(upload_to='images/', default='image.jpg')
    ingredients = HTMLField()
    procedure = HTMLField()
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self, **kwargs):
        return reverse('food', kwargs={'id':self.id})

    def save_food(self):
        self.save()

    def delete_food(self):
        self.delete()


class Comment(models.Model):
    comment = models.TextField(max_length=100)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='comment_owner')
    recipe = models.ForeignKey('Food', on_delete=models.CASCADE, related_name='mycomment')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    

    

