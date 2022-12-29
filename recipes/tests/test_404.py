from django.test import TestCase
from django.urls import reverse

from recipes.models import Category, User, Recipe


class RecipesTest404(TestCase):

    def test_status_code404(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 404)

    def test_createRecipe(self):
        category = Category.objects.create(name='Almoço Grátis')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            email='user@email.com',
            password='123456',
        )
        recipe = Recipe.objects.create(
            title='My Recipe',
            description='Simple Recipe',
            slug='my-recipe',
            preparation_time=2,
            preparation_time_unit='horas',
            servings=4,
            servings_unit='porções',
            preparation_steps='recipe steps',
            preapration_steps_is_html=False,
            is_published=True,
            category=category,
            cover='media/recies/covers/2022/12/28/picanhasuina.jpg',
            author=author,
        )
        response = self.client.get(reverse('recipes:home'))

        self.assertEqual(response.context['recipes'].first().title, 'My Recipe')
        self.assertIn(recipe.title, response.content.decode('utf-8'))