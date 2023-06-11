from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# title
# release_date (default the date of today)
# created_in_country : One to Many relationship with Country (the “nationality of the film”)
# available_in_countries : Many to Many relationship with Country
# category: Many to Many relationship with Category
# director : Many to Many relationship with Director

class Film(models.Model):
    title= models.CharField(max_length=50)
    release_date = models.DateField(default=timezone.now().date())
    created_in_country = models.ForeignKey(Country, related_name='films_created', on_delete=models.SET_NULL, null=True)
    available_in_countries = models.ManyToManyField(Country, related_name='films_available')
    category = models.ManyToManyField(Category, related_name='films')
    director = models.ManyToManyField(Director, related_name='films')


    def __str__(self):
        return self.title


class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating =models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                    MaxValueValidator(5)])
    review_date =  models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.review_text[:20]}...'