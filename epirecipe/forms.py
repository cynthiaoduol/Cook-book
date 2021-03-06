from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Food,Profile,Comment

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','profile_picture','bio')
        exclude = ('user',)


class FoodRecipeForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name','dish_image','ingredients','procedure')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        exclude = ('user','recipe')


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

