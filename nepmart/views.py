from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, this is my first view!")

def house(request):
    return HttpResponse("Input your house name here.")

def index(request):
    return HttpResponse("Print some message here.")
