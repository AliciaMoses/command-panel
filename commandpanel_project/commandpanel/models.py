from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Script(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    code = models.TextField()