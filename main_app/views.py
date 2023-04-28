from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('<p>welcome to the index!</p>')

def about(request):
    return HttpResponse('<h3>About us:</h3><p>This is a website.</p>')