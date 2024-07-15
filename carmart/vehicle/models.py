from django.db import models
from django.contrib.auth.models import User
from brand.models import Brands

class Vehicles(models.Model):
    name = models.CharField(max_length=20)
    details = models.TextField()
    image = models.ImageField(upload_to='posts/media/upload/')
    brand = models.ForeignKey(Brands,on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    vehicles = models.ForeignKey(Vehicles,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f'Comment by {self.name}'