
from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name="home"),
    path('post/<int:pk>',post,name="post"),
    path('login/',login,name="login"),
    
    
]
