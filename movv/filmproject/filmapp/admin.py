from django.contrib import admin

# Register your models here.
from .models import category,film,Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,CategoryAdmin)


class FilmAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','actors','youtubelnk','created','updated']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(film, FilmAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','body','created_on','active')
    list_filter = ('active','created_on')
    search_fields = ('name','email','body')
    actions = ['approve_comments']

    def approve_comments(self,request,queryset):
        queryset.update(active=True)
admin.site.register(Comment,CommentAdmin)