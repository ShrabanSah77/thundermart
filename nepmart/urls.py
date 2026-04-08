from django.urls import path
from . import views  # relative import from the same app

urlpatterns = [
    path('', views.index, name='index'),
    path('signIn_view/', views.signIn_view, name= 'signIn_view'),
    path('Customer/', views.Customer, name = 'Customer'),
    path('Products/', views.Products, name='Products'),
]