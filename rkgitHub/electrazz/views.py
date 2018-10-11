from django.shortcuts import render
from .models import Carousal,News,Fame,Core
# Create your views here.

def index(request):
    car=Carousal.objects.all()
    news=News.objects.all()
    fame=Fame.objects.all()
    core=Core.objects.all()
    caro={'carousal':car,'len':list(range(car.count())),'news':news,'fame':fame,'core':core}
    return render(request,"electrazz/electrazz.html",caro)
