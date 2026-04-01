from django.urls import path
from . import views  # relative import from the same app

urlpatterns = [
    path('', views.home, name='home'),        # URL: /
    path('house/', views.house, name='house'),# URL: /house/
    path('index/', views.index, name='index') # URL: /index/
]