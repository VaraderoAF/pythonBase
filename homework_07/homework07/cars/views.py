from django.shortcuts import render

# Create your views here.

from cars.models import Car


def index(request):
    return render(request, 'cars/index.html')


def car_list(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'cars/list.html', context=context)