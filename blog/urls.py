from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog'),
    path('category/<int:category_id>/', views.category_posts, name='category'),
    path('<int:post_id>/', views.blog_post, name='post')
]
