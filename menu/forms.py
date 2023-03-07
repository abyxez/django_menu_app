from django import forms
from menu.models import Genre

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'parent']