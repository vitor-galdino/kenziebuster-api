from django.db import models


class RatingChoices(models.TextChoices):
    G_OPTION = 'G'
    PG_OPTION = 'PG'
    PG_13_OPTION = 'PG-13'
    R_OPTION = 'R'
    NC_17_OPTION = 'NC-17'


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        null=True,
        choices=RatingChoices.choices,
        default=RatingChoices.G_OPTION,
    )
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='movies'
    )
    users = models.ManyToManyField(
        'users.User', through='MovieOrder', related_name='ordered_movies'
    )


class MovieOrder(models.Model):
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
