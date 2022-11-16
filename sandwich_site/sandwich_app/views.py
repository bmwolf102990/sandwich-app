from django.shortcuts import render
from django.views import View

import random


ingredients = {
    'meats': ['turkey', 'ham', 'chicken', 'liverwurst', 'pastrami', 'veggie burger'],
    'cheeses': ['provolone', 'swiss', 'cheddar', 'pepper jack', 'mozzarella'],
    'toppings': ['lettuce', 'tomato', 'onions', 'pickles', 'mushrooms', 'olives'],
}
# Create your views here.
class SandwichAppView(View):
    def get(self, request):
        return render (
            request = request,
            template_name = 'sandwich_app.html',
            context = {'ingredients': ingredients.keys()},
        )
        
class IngredientsView(View):
    def get(self, request, ingredient_type):
        return render (
            request = request,
            template_name = 'ingredients_list.html',
            context = {
                'ingredients': ingredients[ingredient_type],
                'ingredient_type': ingredient_type,
            },
        )
        
class RandomSandwichView(View):
    def get(self, request):
        return render (
            request = request,
            template_name = 'random_sandwich.html',
            context = {
                'meat': random.choice(ingredients['meats']),
                'cheese': random.choice(ingredients['cheeses']),
                'topping': random.choice(ingredients['toppings']),
            }
        )

class FullMenuView(View):
    def get(self, request):
        return render (
            request = request,
            template_name = 'full_sandwich_menu.html',
            context = {
                'meats': ingredients['meats'],
                'cheeses': ingredients['cheeses'],
                'toppings': ingredients['toppings'],
            }
        )
