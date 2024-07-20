from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    take_personality_test = models.BooleanField(default=False)
    semester = models.IntegerField(null=True, blank=True)
    branch = models.CharField(max_length=100, null=True, blank=True)
