
from .import views
from django.urls import path


app_name='saved_items'

urlpatterns = [

    path('add/<int:film_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('remove/<int:film_id>/',views.cart_remove,name='cart_remove'),
    path('full_remove/<int:film_id>/',views.full_remove,name='full_remove')



]