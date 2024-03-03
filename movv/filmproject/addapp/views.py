from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FilmForm
from filmapp.models import film
# Create your views here.

def add_film(request):
    form = FilmForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("filmapp:allfilmCat")
    return render(request, "add.html", {"form": form})

def delete(request,id):
    if request.method == 'POST':
        Film = film.objects.get(id=id)
        Film.delete()
        return redirect("filmapp:allfilmCat")
    return render(request,'delete.html')


