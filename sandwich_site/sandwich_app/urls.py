from django.urls import path
from sandwich_app.views import SandwichAppView, IngredientsView, RandomSandwichView, FullMenuView

urlpatterns = [
    path('', SandwichAppView.as_view(), name='sandwich_home'),
    path('ingredients/<str:ingredient_type>', IngredientsView.as_view(), name='ingredients_list'),
    path('random/', RandomSandwichView.as_view(), name='random_sandwich'),
    path('menu/', FullMenuView.as_view(), name='full_menu'),
]
