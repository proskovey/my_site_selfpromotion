from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from main.models import Product

def index_page(request):
    template_name = 'main/index.html'
    return render(request, template_name, context={})

def function(request):
    template_name = 'main/func.html'
    return render(request, template_name, context={})

def classes(request):
    template_name = 'main/classes.html'
    return render(request, template_name, context={})

def speech(request):
    template_name = 'main/speech.html'
    return render(request, template_name, context={})