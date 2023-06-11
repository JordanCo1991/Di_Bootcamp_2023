from django.db import models

# Create your models here.


class Students(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    date_joined  = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.first_name



