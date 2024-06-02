from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def index(request):
           return render(request,'Pages/index.html')

def about(request):
    context = {'message': 'Welcome to the about page!'}
    return render(request, 'Pages/about.html', context)