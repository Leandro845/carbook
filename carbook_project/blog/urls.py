from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog-details/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('blogs-per-brand/<int:brand_id>', views.blogs_per_brand, name='blogs_per_brand'),
    path('post-comment/<int:blog_id>', views.post_comment, name='post_comment')
]