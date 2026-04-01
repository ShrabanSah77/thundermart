from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is my first view page!!")

def login_view(request):
    return HttpResponse("This is my second view page!!")

def register_view(request):
    return HttpResponse("This is my third view page!!")