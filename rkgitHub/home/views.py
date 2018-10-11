from django.shortcuts import render
from .models import Carousal


def index(request):
    car = Carousal.objects.all()
    caro = {'carousal': car, 'len': list(range(car.count()))}
    return render(request, "home/home.html", caro)
