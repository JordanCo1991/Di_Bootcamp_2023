from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Film, Category, Country, Director, Review
from .forms import FilmForm, DirectorForm, ReviewForm


class HomePageView(ListView):
    template_name ='films/homepage.html'
    model = Film
    context_object_name = 'films'

class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name ='film/addFilm.html'
    success_url = reverse_lazy('homepage')


class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name ='director/addDirector.html'
    success_url = reverse_lazy('homepage')


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/addReview.html'
    success_url = reverse_lazy('homepage')

    def get_initial(self) -> Dict[str, Any]:
        data = self.request.GET
        film_id = data.get('film_id', None)
        if film_id is not None:
            film_id = int(film_id)
            film = Film.objects.get(id=film_id)
            return {'film': film}
        else:
            return()
