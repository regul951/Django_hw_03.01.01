from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, unique=True)
    price = models.IntegerField(default=0)
    image = models.URLField(max_length=500)
    release_date = models.DateField()
    lte_exists = models.BooleanField()