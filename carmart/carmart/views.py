from django.shortcuts import render,redirect
from vehicle.models import Vehicles
from brand.models import Brands


def home(request,brand_slug = None):
    vehicle = Vehicles.objects.all()
    if brand_slug is not None:
        brand = Brands.objects.get(slug = brand_slug)
        vehicle = Vehicles.objects.filter(brand = brand)
    brands = Brands.objects.all()
    return render(request,"home.html",{'brands': brands,'vehicle':vehicle})