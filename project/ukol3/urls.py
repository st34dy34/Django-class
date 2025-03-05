from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView 

from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),  
    path("profile/", ProfileView.as_view(), name="profile"),  
    path("make_pizza/", make_pizza, name="make_pizza"), 
    
    path("login/", LoginView.as_view(template_name="auth_form.html"), name="pizza_login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="pizza_logout"),
    
    path("registration/", register, name="pizza_registration"),

]
