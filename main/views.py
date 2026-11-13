import requests
from django.shortcuts import render
from blog.models import Articles

# Create your views here.

def index(request):
  news = Articles.objects.order_by('date')
  return render(request, 'main/index.html', {'news': news})

def about(request):
  return render(request, 'main/about.html')