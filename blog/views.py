from datetime import date
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from .models import Author, Tag, Post

posts_list = Post.objects.all()
latest_posts = Post.objects.order_by("-date")

def index(request):
    return render(request, "blog/index.html", {
        "posts": latest_posts,
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": latest_posts,
    })

def post_detail(request, slug):
    # found_post = next(post for post in posts_list if post['slug'] == slug)
    found_post = Post.objects.get(slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": found_post,
    })