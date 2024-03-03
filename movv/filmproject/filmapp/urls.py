from django.urls import path
from . import views
app_name='filmapp'
urlpatterns = [
    path('',views.allfilmCat,name='allfilmCat'),
    path('<slug:c_slug>/', views.allfilmCat, name='films_by_category'),
    path('<slug:c_slug>/<slug:film_slug>/', views.flmDetail, name='filmCatdetail'),
    path('post_detail',views.post_detail,name='post_detail'),
    path('categories',views.catname,name='categories')
]