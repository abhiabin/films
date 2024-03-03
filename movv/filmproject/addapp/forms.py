from django import forms
from filmapp .models import film



class FilmForm(forms.ModelForm):
    class Meta:
        model=film
        fields=['name','slug','description','category','actors','image','youtubelnk']