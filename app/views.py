from django.shortcuts import render
from django.template.context_processors import request

from .models import Car, Category

def home_site(reqeust):
    cars = Car.objects.all()
    category = Category.objects.all()

    return render(request=reqeust, template_name='app/home.html', context={"car":cars,"categories":category})

def category_site(reqeust, pk):
    cars = Car.objects.filter(category_it=pk)
    category = Category.objects.all()

    return render(request=reqeust, template_name='app/category.html', context={"categories":category, "car":cars})

def car_site(reqeust, pk):
    cars = Car.objects.get(id=pk)
    category = Category.objects.all()

    return render(request=reqeust, template_name="app/car.html", context={"car":cars, "categories":category})
