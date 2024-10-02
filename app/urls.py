from django.urls import path
from . import views
from .views import car_create

urlpatterns = [
    path('home/', views.home_site, name="home"),
    path('category/<int:pk>', views.category_site, name="category"),
    path('car/<int:pk>', views.car_site, name='car'),
    path('car_create/', views.car_create, name='car_create')
]
