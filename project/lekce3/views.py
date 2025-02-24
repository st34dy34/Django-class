from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Car
from django.urls import reverse_lazy

# Create your views here.
class CarListView(ListView):
    model = Car 
    template_name = "car_list.html"
    context_object_name = 'cars'
    
class CarCreateView(CreateView):
    model = Car 
    fields = ['brand', 'color']
    template_name = "car_form.html"
    success_url = reverse_lazy('car_list')
    
class CarDetailView(DetailView):
    model = Car 
    template_name = "car_detail.html"
    context_object_name = 'car'
    
class CarUpdateView(UpdateView):
    model = Car 
    fields = ['brand', 'color']
    template_name = "car_form.html"
    success_url = reverse_lazy('car_list')
    
class CarDeleteView(DeleteView):
    model = Car 
    template_name = "car_confirm.html"
    success_url = reverse_lazy('car_list')