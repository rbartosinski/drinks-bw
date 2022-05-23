from django import forms
from .models import requiredUtensil, ingredientType, Ingredients


class DrinkForm(forms.Form):
    name = forms.CharField(max_length=100)
    utensil = forms.ChoiceField(choices=requiredUtensil)


class IngredientForm(forms.Form):
    name = forms.CharField(max_length=100)
    type = forms.ChoiceField(choices=ingredientType)
