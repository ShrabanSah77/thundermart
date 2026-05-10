from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    context = {'user_name': 'Shraban'}
    return render(request, 'index.html', context)

def login_view(request):
    if request.method == ('POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user, 'Logged in successfully')
            return redirect('index') #Redirect to the homepage
        else:
             messages.error(request, 'Invalid username or password')#Return to the invalid pages

    return render(request, 'signIn/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request, 'All fields are required')
            return redirect('register') #Redirect to the register page
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already exists')
            return redirect('register') #Redirect to the register page

        else:
            User.objects.create_user(username = username, email=email, password=password)
            messages.success(request, 'Account created successfully')
            return redirect('login') #Redirect to the login page
        
    return render(request, 'signIn/register.html')

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        messages.success(request, 'Password reset link sent(check console)')
    return render(request, 'signIn/forgot_password.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def customer_list(request):
    customer = Customer.objects.all()
    return HttpResponse(f"{list(customer)}")

def product_list(request):
    products = Product.objects.all()
    return HttpResponse(f"{list(products)}")
