from django.urls import path
from . import views  # relative import from the same app

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name= 'login'),
    path('register/', views.register_view, name='register'),
    path('forgot_password/', views.forgot_password_view, name = 'forgot_password'),
    path('logout/', views.logout_view, name = 'logout'),    
    path('customer_list/', views.customer_list, name = 'customer_list'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name = 'cart'),
    path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
]