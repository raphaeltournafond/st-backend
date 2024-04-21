import json
from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    data = models.TextField()

