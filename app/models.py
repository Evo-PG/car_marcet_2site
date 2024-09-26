from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/image_car")
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(max_length=1000)
    category_it = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.make}, {self.model}"
