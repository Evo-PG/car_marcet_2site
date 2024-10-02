from django.shortcuts import render, redirect
from django.template.context_processors import request

from .models import Car, Category

def home_site(reqeust):
    cars = Car.objects.all()
    category = Category.objects.all()

    if "search" in reqeust.GET:
        search = reqeust.GET["search"]
        cars = Car.objects.filter(make__icontains=search)

    return render(request=reqeust, template_name='app/home.html', context={"cars":cars,"categories":category})

def category_site(reqeust, pk):
    cars = Car.objects.filter(category_it=pk)
    category = Category.objects.all()

    return render(request=reqeust, template_name='app/category.html', context={"categories":category, "cars":cars})

def car_site(reqeust, pk):
    cars = Car.objects.get(id=pk)
    category = Category.objects.all()

    return render(request=reqeust, template_name="app/car.html", context={"car":cars, "categories":category})

def car_create(reqeust):
    categories_all = Category.objects.all()

    if reqeust.method    == "POST":
        make = reqeust.POST["make"]
        model = reqeust.POST["model"]
        image = reqeust.POST["image"]
        year = reqeust.POST["year"]
        price = reqeust.POST["price"]
        description = reqeust.POST["description"]
        category = reqeust.POST["category"]

        categories = Category.objects.get(id=int(category))

        car = Car(
            make=make,
            model=model,
            image=image,
            year=year,
            price=price,
            description=description,
            category_it=categories,
        )
        car.save()

        return redirect('home')

    return render(request=reqeust, template_name='app/create_car.html', context={"categories":categories_all})
