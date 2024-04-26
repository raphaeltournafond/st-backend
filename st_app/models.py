from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):

    class Meta:
        app_label = 'st_app'
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    data = models.TextField()

