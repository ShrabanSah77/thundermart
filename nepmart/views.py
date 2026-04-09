from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Product

# Create your views here.
def index(request):
    context = {'user_name': 'Shraban'}
    return render(request, 'index.html', context)

def signIn_view(request):
    return HttpResponse("This is my second view page!!")

def customer_list(request):
    customer = Customer.objects.all()
    return HttpResponse(f"{list(customer)}")

def product_list(request):
    products = Product.objects.all()
    return HttpResponse(f"{list(products)}")
