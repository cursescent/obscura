from django.db import models

class Movie(models.Model):
    movieid = models.IntegerField()
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genres = models.CharField(max_length=100)
    duration = models.IntegerField()
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    starring = models.CharField(max_length=500)
    sources = models.JSONField()

class Review(models.Model):
    movieid = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.CharField(max_length=500)
    source = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
