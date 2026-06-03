from ingredient import Ingredient

class ShoppingList:
    def __init__(self):
        self._items = []
    def add_recipe(self, recipe, portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled = recipe.scale(portions)
        for ing in scaled.ingredients:
            self._items.append((ing, recipe.title))
    def remove_recipe(self, title):
        new_items = []
        for item in self._items:
            if item[1] != title:
                new_items.append(item)
        self._items = new_items
    def get_list(self):
        summary = {}
        for ing, _ in self._items:
            key = (ing.name, ing.unit)
            if key in summary:
                summary[key] += ing.quantity
            else:
                summary[key] = ing.quantity
        result = []
        for (name, unit), qty in summary.items():
            result.append(Ingredient(name, qty, unit))
        result.sort(key=lambda x: x.name)
        return result
    def __add__(self, other):
        new_list = ShoppingList()
        new_list._items = self._items.copy()
        new_list._items.extend(other._items)
        return new_list
