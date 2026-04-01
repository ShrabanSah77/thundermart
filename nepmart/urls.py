from django.urls import path
from . import views

urlpattern =[
    path('', views.home),
    path('house/', views.house, name='house'),
    path('index/', views.index, name='index'),
]
