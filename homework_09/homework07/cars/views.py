from django.shortcuts import render
from django.views.generic import ListView, DetailView

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


class CarList(ListView):
    template_name = 'cars/car_list_view.html'
    model = Car
    queryset = Car.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs


class CarDetail(DetailView):
    template_name = 'cars/car_detail_view.html'
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
