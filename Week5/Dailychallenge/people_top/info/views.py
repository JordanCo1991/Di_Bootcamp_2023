from django.shortcuts import render
from data import people
# Create your views here.


def people_view(request):
    people_sorted = sorted(people, key=lambda person:['age'])
    context = {'people_list': people_sorted}
    return render(request, 'people_list.html', context)

def  person_view(request, id: int):
    person = None
    for p in people:
        if p ['id'] == id:
            person = p
            break
    context = {'person_instance': person}
    return render(request,'person.html', context)