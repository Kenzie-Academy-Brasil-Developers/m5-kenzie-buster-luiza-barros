from django.db import models


class RatingChoices(models.TextChoices):
    PG = ("PG",)
    PG13 = ("PG-13",)
    R = ("R",)
    NC17 = ("NC-17",)
    DEFAULT = "G"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        null=True,
        choices=RatingChoices.choices,
        default=RatingChoices.DEFAULT,
    )
    synopsis = models.TextField(null=True, default=None)
    added_by = models.EmailField()

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
        blank=True,
        null=True,
    )
