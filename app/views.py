from django.shortcuts import render, redirect
from .models import Car, Category
from .forms import CarCreateForm, UserRegisterForm

# Home
def home_site(reqeust):
    cars = Car.objects.all()
    category = Category.objects.all()

    if "search" in reqeust.GET:
        search = reqeust.GET["search"]
        cars = Car.objects.filter(make__icontains=search)

    return render(request=reqeust, template_name='app/home.html', context={"cars":cars,"categories":category})

# site search car
def category_site(reqeust, pk):
    cars = Car.objects.filter(category_it=pk)
    category = Category.objects.all()

    return render(request=reqeust, template_name='app/category.html', context={"categories":category, "cars":cars})

def car_site(reqeust, pk):
    cars = Car.objects.get(id=pk)
    category = Category.objects.all()

    if reqeust.method == "POST":
        cars.make = reqeust.POST["make"]
        cars.model = reqeust.POST["model"]
        cars.year = reqeust.POST["year"]
        cars.price = reqeust.POST["price"]
        cars.description = reqeust.POST["description"]

        cars.save()


    return render(request=reqeust, template_name="app/car.html", context={"car":cars, "categories":category})

# create car

def car_create(reqeust):
    categories_all = Category.objects.all()

    if reqeust.method == "POST":
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

def car_create2(request):
    if request.method == 'POST':
        form = CarCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')

    form = CarCreateForm()

    return render(request, 'app/car_create2.html', {'form': form})

# User

def user_create(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    form = UserRegisterForm()

    return render(request, 'app/user_create.html', {'form': form})




