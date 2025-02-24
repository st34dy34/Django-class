from django.urls import path, include
from .views import *


urlpatterns = [
    path('jacket/', JacketListView.as_view(), name="jacket_list"),
    path('jacket/<int:pk>', JacketDetailView.as_view(), name="jacket_detail"),
    path('add/', JacketCreateView.as_view(), name="jacket_create"),
    path('update/<int:pk>', JacketUpdateView.as_view(), name="jacket_update"),
    path('delete/<int:pk>', JacketDeleteView.as_view(), name="jacket_delete"),
]