from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.TextField(default='')
    detail = models.TextField(default='')
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name