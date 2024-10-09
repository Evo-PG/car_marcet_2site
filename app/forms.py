from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Car

# car
class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["make", "model", "image", "year", "price", "description", "category_it"]

# user
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", )

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    password = forms.CharField(widget=forms.PasswordInput)