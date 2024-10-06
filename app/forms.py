from django import forms
from .models import Car

class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["make", "model", "image", "year", "price", "description", "category_it"]



