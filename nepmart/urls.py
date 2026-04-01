from django.urls import path
from . import views

urlpattern =[
    path('', views.home),
    # path('house/', views.house),
    # path('index/', views.index),
]
