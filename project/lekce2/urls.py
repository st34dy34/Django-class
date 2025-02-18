from django.urls import path, include
from .views import *


urlpatterns = [
    path('get_form/', get_form, name="get-form"),
    path('submit_form/', submit_form, name="submit-form"),
    path('post_form/', post_form, name="post-form"),
    path('task/', task, name="task"),
    path('task_submit/', task_submit, name="task_submit"),
    path('task2_submit/', task2_submit, name="task2_submit"),
    
]