from django.contrib import admin
from django.urls import path
from .view import hello_word

urlpatterns = [
    path('hello/', hello_word),
    path('admin/', admin.site.urls),
]
