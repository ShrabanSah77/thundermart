from django.urls import path
from . import views  # relative import from the same app

urlpatterns = [
    path('', views.index, name='index'),
    path('signIn_view/', views.signIn_view, name= 'signIn_view'),
    path('customer_list/', views.customer_list, name = 'customer_list'),
    path('product_list/', views.product_list, name='product_list'),
]