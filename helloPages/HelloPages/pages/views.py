from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def root(request):
    return render(request,'pages/hello.html')

def block(request):
    return render(request, 'pages/inherited.html')
