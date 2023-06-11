from typing import Any, Dict
from django import forms
from .models import Category, Post

class SearchForm(forms.Form):
    query = forms.CharField(max_length=20)
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # exclude = ('author', )
        widgets = {
            'author': forms.HiddenInput(),
            'content': forms.Textarea(attrs={'rows': 3,
                                             'class': 'content_class'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' in title:
            raise forms.ValidationError('Cannot include Django in the title')
        else:
            return title
        
    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data['content']
        author = cleaned_data['author']

        if author.user.is_staff and 'Django' in content:
            raise forms.ValidationError("Cannot be Admin and write about Django")
        else:
            cleaned_data


CategoryFormSet = forms.modelformset_factory(model=Category,
                                             form=CategoryForm,
                                             extra=0)


# CategoryRelatedFormSet = forms.inlineformset_factory(Post, Category, form = CategoryForm, extra=0)
