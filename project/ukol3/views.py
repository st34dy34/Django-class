from django.shortcuts import render, redirect
from django.contrib.admindocs.views import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django import forms
from .models import Pizza

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect("home")  
    else:
        form = UserCreationForm()
    
    return render(request, "auth_form.html", {"form": form})  

@login_required
def make_pizza(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.user = request.user  # Set the user to the currently logged-in user
            ingredients = []

            if pizza.cheese:
                ingredients.append("cheese")
            if pizza.ham:
                ingredients.append("ham")
            ingredients_str = ", ".join(ingredients)

            # Save ingredients in a cookie
            response = set_cookie(request, ingredients_str)
            pizza.save()  # Save pizza with the associated user
            print(f"Saving pizza {ingredients_str}")
            return response
    else:
        ingredients_str = get_cookie(request)

        # Initialize fields based on cookie data
        cheese = "cheese" in ingredients_str
        ham = "ham" in ingredients_str

        # Initialize the form with the values from the cookie
        form = PizzaForm(initial={'cheese': cheese, 'ham': ham})
    
    return render(request, "make_pizza.html", {"form": form})


def set_cookie(request, ingredients):
    response = HttpResponse("Cookie Set!")
    response.set_cookie("ingredients", ingredients, max_age=60*60*24)  
    return response

def get_cookie(request):
    ingredients = request.COOKIES.get("ingredients", "")  
    return ingredients


class HomeView(TemplateView):
    template_name = "home.html"
    


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        pizzas = Pizza.objects.filter(user=user)
        
        context["pizzas"] = pizzas
        return context


    
class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["cheese", "ham"] 
        exclude = ['user']
        
