from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
from .models import Recipe
from django.contrib.auth.models import User

def home(request):
    recipes = Recipe.objects.filter(
        is_published=True,
    )
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
        ).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': Recipe.objects.get(id=id),
        'is_detail_page': True,
    })

def contact(request):
    return render(request, 'recipes/contact.html')

def about(request):
    return render(request, 'recipes/pages/home.html', context={ 'msg':'SOBRE!' })

def email_validation(request):
    return render(request, 'recipes/pages/email-validation.html', context={
        'user': 'Ferdinandy',
        'link': 'https://www.google.com',
    })