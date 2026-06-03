import pytest
from ingredient import Ingredient
from recipe import Recipe
from shopping_list import ShoppingList
from dietary_recipe import DietaryRecipe

def test_ingredient_creation():
    ing = Ingredient("Мука", 500, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500
    assert ing.unit == "г"

def test_ingredient_str():
    ing = Ingredient("Мука", 500, "г")
    assert str(ing) == "Мука: 500.0 г"

def test_ingredient_eq():
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Мука", 1000, "г")
    ing3 = Ingredient("Сахар", 500, "г")
    assert ing1 == ing2
    assert ing1 != ing3

def test_recipe_add_ingredient():
    recipe = Recipe("Тест")
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Мука", 300, "г")
    recipe.add_ingredient(ing1)
    recipe.add_ingredient(ing2)
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 800

def test_recipe_scale():
    recipe = Recipe("Тест", [Ingredient("Мука", 500, "г")])
    scaled = recipe.scale(2)
    assert scaled.ingredients[0].quantity == 1000
    assert recipe.ingredients[0].quantity == 500
