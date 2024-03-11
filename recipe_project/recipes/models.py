from django.db import models

# Create your models here.
# recipes/models.py
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    description = models.TextField()
    rating = models.FloatField(default=0)
    reviews = models.ManyToManyField('Review', related_name='recipe_reviews', blank=True)

class Review(models.Model):
    user = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.FloatField()
