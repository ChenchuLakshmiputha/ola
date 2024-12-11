from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def veg(request):
    return HttpResponse('<h1>Life of pure vegitarians is worst.</h1>')
