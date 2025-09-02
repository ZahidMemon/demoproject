from django.contrib import admin
from .models import Home
from .models import Blog
from .models import Contact


# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display=['title','info']

class BlogAdmin(admin.ModelAdmin):
    list_display=['name','age']

class ContactAdmin(admin.ModelAdmin):
    list_display=['number','email']

admin.site.register(Home,HomeAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Contact,ContactAdmin)