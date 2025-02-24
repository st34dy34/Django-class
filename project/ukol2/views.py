from django.shortcuts import render
from django.urls import reverse_lazy
from django import forms
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Jacket 

# Create your views here.

class JacketListView(ListView):
    model = Jacket
    template_name = "jacket_list.html"
    context_object_name = "jackets"

class JacketForm(forms.ModelForm):
    class Meta:
        model = Jacket
        fields = ['brand', 'color']

class JacketCreateView(CreateView):
    model = Jacket
    form_class= JacketForm
    template_name = "jacket_add.html"
    success_url = reverse_lazy('jacket_list')
    

class JacketDetailView(DetailView):
    model = Jacket
    template_name = "jacket_detail.html"
    
class JacketUpdateView(UpdateView):
    model = Jacket 
    fields = ['brand', 'color']
    template_name = "jacket_add.html"
    success_url = reverse_lazy('jacket_list')
    
class JacketDeleteView(DeleteView):
    model = Jacket 
    template_name = "jacket_confirm.html"
    success_url = reverse_lazy('jacket_list')