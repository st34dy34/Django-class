from django.urls import path, include
from .views import *


urlpatterns = [
     path('list/', CarListView.as_view(), name="car_list"),
     path('list/<int:pk>', CarDetailView.as_view(), name="car_detail"),
     path('add/', CarCreateView.as_view(), name="car_create"),
     path('update/<int:pk>', CarUpdateView.as_view(), name="car_update"),
     path('delete/<int:pk>', CarDeleteView.as_view(), name="car_delete"),
]