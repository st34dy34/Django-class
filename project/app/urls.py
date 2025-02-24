from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('fake/<int:id>', views.fake, name="fake-detail"),
    path('ukol', views.ukol, name="ukol"),
    path('ukol2', views.ukol2, name="ukol2"),
]