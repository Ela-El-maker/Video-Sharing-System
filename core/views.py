from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepage(request):
    return render(request, 'test_temp/index.html')

def contact(request):
    return render(request, 'test_temp/contact.html')

def aboutpage(request):
    return render(request, 'test_temp/about.html')