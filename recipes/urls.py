from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact),
    path('about/', views.about),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
    path('category/<int:category_id>/', views.category, name='category'),
    path('emailvalidation/', views.email_validation, name='email_validation')
]