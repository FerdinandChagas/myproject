from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact),
    path('about/', views.about),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]