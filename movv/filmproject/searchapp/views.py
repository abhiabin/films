from django.shortcuts import render
from filmapp.models import film
from django.db.models import Q

# Create your views here.



def searchResult(request):
    films=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        films=film.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request,'search.html',{'query':query,'films':films})