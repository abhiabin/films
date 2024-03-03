from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import film,category,Comment
from.forms import CommentForm
# Create your views here.
def allfilmCat(request,c_slug=None):
    c_page=None
    films=None
    if c_slug != None:
        c_page= get_object_or_404(category,slug=c_slug)
        films=film.objects.all().filter(category=c_page)

    else:
        films=film.objects.all().filter()

    return render(request,'category.html',{'category':c_page,'films':films})

def flmDetail(request,c_slug,film_slug):
    try:
        Film=film.objects.get(category__slug=c_slug,slug=film_slug)
    except Exception as e:
        raise e
    return render(request,'film.html',{'film':Film})

def post_detail(request):
    new_comment = None
    comments = Comment.objects.all()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,'comment.html', {'comments':comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def catname(request):
    categories=category.objects.all()

    return render(request,'cat_name.html',{'categories':categories})