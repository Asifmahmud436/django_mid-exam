from django.db import models

class Brands(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100,unique=True,blank=True,null=True)

    def __str__(self):
        return self.name
