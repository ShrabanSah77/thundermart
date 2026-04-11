from django.urls import path
from . import views  # relative import from the same app

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name= 'login'),
    
    path('customer_list/', views.customer_list, name = 'customer_list'),
    path('product_list/', views.product_list, name='product_list'),
]