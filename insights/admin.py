from turtle import pos
from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):  #ADMIN PANEL CUSTOMIZED OF PRODUCTLIST
    list_display = ('id','title','category','upload_in')
    list_display_links = ('id','title')  #eita diye product edit kora jay
    list_filter = ('category','upload_in')
    search_fields = ('title','category')
    
admin.site.register(Category)
admin.site.register(Post,PostAdmin)

