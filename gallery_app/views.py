from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World! from Phat")
# Create your views here.


def index(request):
    return render(request, 'index.html')