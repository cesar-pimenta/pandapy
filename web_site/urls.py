from django.urls import path, include
from .views import index_blog, post_detail

urlpatterns = [
    path('', index_blog, name='init_blog'),
    path('post/<int:id>/', post_detail, name='post_detail'),
]