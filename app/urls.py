from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_site, name="home"),
    path('category/<int:kd>', views.category_site, name="category")
]
