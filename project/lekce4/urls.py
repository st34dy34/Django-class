from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('cookies/', TemplateView.as_view(template_name="cookies.html"), name="cookies"),
    path('add_cookies/', create_cookie, name="create_cookie"),
    path('show_cookies/', get_cookie, name="show_cookie"),
    path('delete_cookies/', delete_cookie, name="delete_cookie"),
]