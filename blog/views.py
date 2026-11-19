from django.shortcuts import render, get_object_or_404
from .models import Articles, Category

# Create your views here.

def blog_home(request):
  news = Articles.objects.order_by('date')
  return render(request, 'blog/index.html', {
    'news': news,
    'page_title': 'News',
  })


def category_posts(request, category_id):
  category = get_object_or_404(Category, pk=category_id)
  news = Articles.objects.filter(categories=category).order_by('date')
  return render(request, 'blog/index.html', {
    'news': news,
    'page_title': category.title,
  })

def blog_post(request, post_id):
  post = get_object_or_404(Articles, pk=post_id)
  return render(request, 'blog/post.html', {'post': post})
