from django.shortcuts import render
from .models import Car, Category

def home_site(reqeust):
    cars = Car.objects.all()
    category = Category.objects.all()

    return render(request=reqeust, template_name='app/home.html', context={"car":cars,"categories":category})

def category_site(reqeust, kd):
    category = Category.objects.filter(id=kd)

    return render(request=reqeust, template_name='app/category.html', context={"category":category})
