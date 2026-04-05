from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {'user_name': 'Shraban'}
    return render(request, 'index.html', context)

def login_view(request):
    return HttpResponse("This is my second view page!!")

def register_view(request):
    return HttpResponse("This is my third view page!!")
