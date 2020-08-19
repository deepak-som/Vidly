from django.db import models
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=255)
    desh = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    star = models.CharField(max_length=255)
    number_in_stock = models.IntegerField()
    daily_bhada = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
