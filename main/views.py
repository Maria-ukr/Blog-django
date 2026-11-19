import requests
from django.shortcuts import render
from blog.models import Category

# Create your views here.

def index(request):
  categories = Category.objects.all()
  return render(request, 'main/index.html', {'categories': categories})

def about(request):
  return render(request, 'main/about.html')