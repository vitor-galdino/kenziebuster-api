from django.db import models


class Rating_Choices(models.TextChoices):
    G_OPTION = 'G'
    PG_OPTION = 'PG'
    PG_13_OPTION = ' PG-13'
    R_OPTION = 'R'
    NC_17_OPTION = 'NC-17'


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True)
    rating = models.CharField(
        max_length=20, choices=Rating_Choices.choices, default=Rating_Choices.G_OPTION
    )
    synopsis = models.TextField(null=True)
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='movies'
    )
