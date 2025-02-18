from django.urls import path, include
from .views import *


urlpatterns = [
    path('', homework, name="homework"),
    path('show-message/', show_message, name='show_message'),
    path('choose-category/', choose_category, name='choose_category'),
    path('feedback/', feedback_view, name='feedback'),  
    path('static-page/', StaticPageView.as_view(), name='static_page'),
    path('contact/', ContactView.as_view(), name='contact'),
]