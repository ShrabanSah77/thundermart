from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Product

# Create your views here.
def index(request):
    context = {'user_name': 'Shraban'}
    return render(request, 'index.html', context)

def login_view(request):
    if request.method == ('POST'):
        username = request.POST.get('username: ')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #Redirect to the source page

        else:
            #Return to the invalid pages


            return redirect('home')
    return render(request, 'signIn/login.html')

def register_view(request):
    return render(request, 'signIn/register.html')

def forgotPassword_view(request):
    return render(request, 'forgotpassword.html')

def customer_list(request):
    customer = Customer.objects.all()
    return HttpResponse(f"{list(customer)}")

def product_list(request):
    products = Product.objects.all()
    return HttpResponse(f"{list(products)}")
