from django.db import models
from filmapp.models import film
# Create your models here.

class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateField(auto_now_add=True)

    class Meta:
        db_table='saved_items'
        ordering=['date_added']
    def __str__(self):
        return '{}'.format(self.cart_id)
class CartItem(models.Model):
    Product=models.ForeignKey(film,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='savedItem'
    def __str__(self):
        return '{}'.format(self.Product)