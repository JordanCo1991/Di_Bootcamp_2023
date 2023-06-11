from django.db import models

# Create your models here.



CATEGORY_CHOICES =(
    ('Dj', 'Django'),
    ('Js', 'Javascript'),
    ('C', 'C'),
)


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    publish_date = models.DateTimeField(auto_now_add=True)  #When Creating
    last_updated = models.DateTimeField(auto_now=True)      ##When Updating


    def __str__(self):
        return self.title