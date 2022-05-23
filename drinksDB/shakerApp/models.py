from django.db import models


ingredientType = (
    (1, "Alcohol"),
    (2, "Soft drink"),
    (3, "Fruit"),
    (4, "Spice")
)

requiredUtensil = (
    (1, "Shaker"),
    (2, "Glass")
)


class Ingredients(models.Model):
    type = models.IntegerField(choices=ingredientType)
    name = models.CharField(max_length=100)


class DrinkRecipe(models.Model):
    drinkName = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredients)
    preparation = models.CharField(max_length=1000)
