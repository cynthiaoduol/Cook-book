from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import SignUpForm,FoodRecipeForm
from django.contrib.auth.models import User
from .models import Food



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


def single_recipe(request,food_id):
    food = Food.objects.get(id=food_id)
    params = {'hood':hood}
    return render(request,'single-recipe.html',params)
    




        