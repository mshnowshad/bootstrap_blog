from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request,'files/home.html')



def post(request):
    return render(request,'files/post.html')
