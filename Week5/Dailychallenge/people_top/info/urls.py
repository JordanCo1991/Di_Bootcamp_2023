from django.urls import path
from .views import people_view, person_view


urlpatterns = [
    path('', people_view),
    path('<int:id>', person_view(request)),
]
