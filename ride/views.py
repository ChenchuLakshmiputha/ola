from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def nonveg(request):
    return HttpResponse('<h1>Life of Nonvegitarians is beautiful. </h1>')