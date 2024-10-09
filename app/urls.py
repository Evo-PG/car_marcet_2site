from django.urls import path
from . import views
from .views import car_create

urlpatterns = [
    # home
    path('home/', views.home_site, name="home"),
    # search car
    path('category/<int:pk>/', views.category_site, name="category"),
    path('car/<int:pk>/', views.car_site, name='car'),
    # create car
    path('car_create/', views.car_create, name='car_create'),
    path('car_create2/', views.car_create2, name='car_create2'),
    # user
    path('register/', views.user_create, name='register')

]
