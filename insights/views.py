from django.shortcuts import render,redirect
from .models import Category,Post
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def search(request):
    if request.method == 'POST':  # Corrected the case of 'POST'
        searched = request.POST.get('searched')  # Corrected retrieving data from request
        prods = Post.objects.filter(
            Q(title__icontains=searched) |
            Q(tags__icontains=searched) |
            Q(category__name__icontains=searched)
        )
        
        if not prods:
            messages.success(request, "Hmm, Your Searched Item Isn't in Our Blog. Keep Scrolling for More!")  # Corrected error message
            return redirect('home')
        else:
            return render(request, 'files/search.html', {'searched': searched, 'prods': prods})
    else:
        return render(request, 'files/search.html')

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