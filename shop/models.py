from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(default='', max_length=200, unique=True)
    detail = models.TextField(default='')
    price = models.FloatField(default=0)
    in_stock = models.BooleanField(default=False)
    show = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name