from django.db import models
from django.contrib.auth.models import User

# Create your models here.

OPTION_TYPE= (
    ('sun', 'sunny'),
    ('cloud', 'cloudy'),
    ('wind', 'windy'),
    ('storm', 'stormy'),
    ('rain', 'rainy')
)
    

class Report(models.Model):
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=5, choices=OPTION_TYPE)
    
    def __str__(self):
        return self.type


class Forecaster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
