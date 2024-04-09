from django.shortcuts import render
from .models import Category,Post
from django.core.paginator import Paginator
# Create your views here.



def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    if request.htmx:
        return render(request, 'files/home.html',{'posts':page_obj})
    


    dic = {
        'posts':page_obj,
     }
    return render(request,'files/home.html',dic)



def post(request,pk):
    post = Post.objects.get(id=pk)
    return render(request,'files/post.html',{'post':post})
def login(request):
    return render(request,'files/login.html')