from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Script(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    code = models.TextField()
    
class Parameter(models.Model):
    script = models.ForeignKey(Script, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    value = models.CharField(max_length=100)
    
class UserScript(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    script = models.ForeignKey(Script, on_delete=models.CASCADE)
    parameters = models.ManyToManyField(Parameter)