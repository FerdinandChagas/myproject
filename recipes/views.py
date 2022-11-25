from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/pages/home.html', {'name':'Ferdinandy'})

def recipe(request,id):
    return render(request, 'recipes/pages/home.html', {'name':'Ferdinandy'})

def contact(request):
    return render(request, 'recipes/contact.html')

def about(request):
    return HttpResponse('SOBRE!')