from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product, Customer

# Create your views here.
# Index View
def index(request):
    context = {'user_name': 'Shraban'}
    return render(request, 'index.html', context)

# Login View

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

# Register View

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

# Forgot password view

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        messages.success(request, 'Password reset link sent(check console)')
    return render(request, 'signIn/forgot_password.html')

# Logout View

def logout_view(request):
    logout(request)
    return redirect('login')

# Customer View

def customer_list(request):
    customer = Customer.objects.all()
    return HttpResponse(f"{list(customer)}")

# Add to cart view

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    if srt(product_id) in cart:
        cart[srt(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('product_list')

# Cart View

def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id, qty in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.prict * qty

        products.append({
            'product': product,
            'quantity': qty,
            'subtotal': subtotal
        })

        total += subtotal

    return render(request, 'product/cart.html', {
        'items': products,
        'total': total
    })

# Remove from cart view

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('cart')