from django.shortcuts import render
from .models import all_posts


def get_date(post):
  return post['date']

def home(request):
  sorted_posts = all_posts
  sorted_posts.sort(key=lambda post: post['date'])
  latest_post = sorted_posts[-3:]
  return render(request, 'blog/home.html', { 'posts': latest_post })


def list(request):
  posts = all_posts
  return render(request, 'blog/list.html', { 'posts': posts })


def detail(request, slug):
  choosen = next(filter(lambda post:post['slug'] == slug, all_posts))
  # selected_post = next(post for post in all_posts if post['slug'] == slug)
  return render(request, 'blog/detail.html', { 'post': choosen })
