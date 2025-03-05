from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Pizza(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pizzas")
    cheese = models.BooleanField(default=False)
    ham = models.BooleanField(default=False)

    def __str__(self):
        return f"Pizza (Cheese: {self.cheese}, Ham: {self.ham}) - {self.user.username}"