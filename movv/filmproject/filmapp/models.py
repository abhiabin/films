from django.db import models
from django.urls import reverse

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('filmapp:films_by_category',args=[self.slug])

    def __str__(self):
        return  '{}'.format(self.name)

class film(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    actors=models.CharField(max_length=250,unique=True)
    image=models.ImageField(upload_to='film',blank=True)
    youtubelnk=models.CharField(max_length=250,unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('filmapp:filmCatdetail',args=[self.category.slug,self.slug])

    class Meta:
        ordering=('name',)
        verbose_name='film'
        verbose_name_plural='films'

    def __str__(self):
        return  '{}'.format(self.name)





class Comment(models.Model):
    name=models.CharField(max_length=80)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)
    
    class Meta:
        ordering=['created_on']
    def __str__(self):
        return 'comment {} by {}'.format(self.body,self.name)