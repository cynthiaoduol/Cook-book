from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login
from .forms import SignUpForm,FoodRecipeForm,UpdateProfileForm,CommentForm
from django.contrib.auth.models import User
from .models import Food,Profile,Comment



def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm()
    return render(request, 'create_profile.html', {'form': form})


def profile(request, username):
    return render(request, 'profile.html')


def recipes(request):
    all_recipes = Food.objects.all()
    all_recipes = all_recipes[::-1]
    params = {
        'all_recipes': all_recipes,
    }
    return render(request, 'recipes.html', params)


def add_recipe(request):
    if request.method == 'POST':
        form = FoodRecipeForm(request.POST,request.FILES)
        if form.is_valid():
            food = form.save(commit=False)
            food.save()
            return redirect('food')
    else:
        form = FoodRecipeForm()
    return render(request,'newrecipe.html',{'form':form})  


def single_recipe(request,recipe_id):
    recipe = Food.objects.get(id=recipe_id)
    comment = Comment.objects.filter(recipe=recipe)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            coment_form = form.save(commit=False)
            coment_form.recipe = recipe
            coment_form.user = request.user.profile
            coment_form.save()
            return redirect('single_recipe',recipe.id)
    else:
        form = CommentForm()
    params = {
        'recipe':recipe,
        'form':form,
        'comment':comment
    }
    return render(request,'single-recipe.html',params)
    




        