from django.urls import path
from . import views

app_name='addapp'
urlpatterns = [

           path('',views.add_film,name='add_film'),
           path('delete/<int:id>/',views.delete,name='delete')
]