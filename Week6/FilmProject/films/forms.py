from django import forms
from .models import Film, Director, Review
from django.utils import timezone


class FilmForm(forms.ModelForm):
   
   class Meta:
    model = Film
    fields = '__all__'
    widgets = {
        'release_date': forms.DateInput(attrs={'type': 'date'})
    }


    def clean_release_date(self):
        today = timezone.now().date()
        release_date = self.cleaned_data.get('release_date')
        if release_date > today:
            raise forms.ValidationError("Release date can not be in the future !")


class DirectorForm(forms.ModelForm):

    class Meta:
        model = Director
        fields = '__all__'

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'
    rating = forms.ChoiceField(choices=((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')), widget=forms.RadioSelect(attrs={'class': 'inline'}))
        

