# This file contains Host model for this project

from django.db import models
from django.contrib.auth.models import User


# Host model is extended from django inbuilt User model
class Host(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_Number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username}"
