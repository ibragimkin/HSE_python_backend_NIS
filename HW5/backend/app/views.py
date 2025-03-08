from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    posts = Post.objects.all()
    # Формируем строку с названиями постов для простоты
    posts_titles = ", ".join([post.title for post in posts])
    return HttpResponse(f"Posts: {posts_titles}")
