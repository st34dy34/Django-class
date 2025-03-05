from django.urls import path
from django.views.generic import TemplateView
from .views import add_perm, restricted_view

urlpatterns = [
    path('', TemplateView.as_view(template_name="lek5.html"), name="lek5_view"),
    path('add_perm', add_perm, name="add_perm"),
    path('restrict', restricted_view, name="restrict"),
]