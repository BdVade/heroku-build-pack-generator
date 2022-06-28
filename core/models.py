from django.db import models

# Create your models here.


class BuildPack(models):
    name = models.CharField(max_length=500)
    image = models.ImageField(null=True)
    description = models.CharField(max_length=5000)
    buildpack = models.FileField()