from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Car

class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["make", "model", "image", "year", "price", "description", "category_it"]


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", )

