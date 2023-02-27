from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie


class User(AbstractUser):
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(null=True)
    is_employee = models.BooleanField(null=True, default=False)

    movies_orders = models.ManyToManyField(
        Movie, through="MovieOrder", related_name="users_orders"
    )


class MovieOrder(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
