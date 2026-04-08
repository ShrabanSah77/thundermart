from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .models import Products

# Create your views here.
def index(request):
    context = {'user_name': 'Shraban'}
    return render(request, 'index.html', context)

def signIn_view(request):
    return HttpResponse("This is my second view page!!")

def customer(request):
    Customer = Customer.objects.all()
    return HttpResponse(Customer)

def product_list(request):
    Products = Products.objects.all()
    return HttpResponse(Products)
