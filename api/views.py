from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    message = "Hello world!!!"
    return  HttpResponse(message)
# Create your views here.
