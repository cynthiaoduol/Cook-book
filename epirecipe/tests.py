from django.test import TestCase
from .models import Profile,Food,Comment
from django.contrib.auth.models import User

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username = 'doryn',email= 'doryn@gmail.com', password = '3rt5')
        self.user.save()    
        
        self.profile = Profile(user=self.user, name='doryn', bio='my bio',profile_picture = 'image.png')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
        
    def test_save_profile(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)
        
    def test_delete_profile(self):
        profile = Profile.objects.all().delete()
        self.assertTrue(len(profile)>0)
        
    def tearDown(self):
        Profile.objects.all().delete()
        
      
class TestFood(TestCase):
    def setUp(self):
        self.user = User(username = 'doryn',email= 'doryn@gmail.com', password = '3rt5')
        self.user.save() 

        self.food = Food(name = 'French Fries',dish_image='chips.png',ingredients='potatoes,2kg oil',procedure='pell the potatoes,boil oil,add potatoes', favourite='self.user')
        self.food.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.food, Food))
        
    def test_save_food(self):
        recipe = Food.objects.all()
        self.assertTrue(len(recipe)>0)
        
    def test_delete_food(self):
        recipe = Food.objects.all().delete()
        self.assertTrue(len(recipe)>0)


class TestComment(TestCase):
    def setUp(self):
        self.user = User(username = 'doryn',email= 'doryn@gmail.com', password = '3rt5')
        self.user.save()

        self.recipe = Food(name = 'French Fries',dish_image='chips.png',ingredients='potatoes,2kg oil',procedure='pell the potatoes,boil oil,add potatoes', favourite='self.user')
        self.food.save()

        self.coment = Comment(comment='this is nice',user='self.user',recipe='self.recipe',date='2-3-2000')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.coment, Comment))

    def test_save_comment(self):
        coment = Comment.objects.all()
        self.assertTrue(len(coment)>0)

    def test_delete_comment(self):
        coment = Comment.objects.all().delete()
        self.assertTrue(len(coment)>0)


    




        
        
