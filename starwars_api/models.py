from django.db import models


class Rating(models.Model):
    character_id = models.IntegerField()
    rating = models.IntegerField()
