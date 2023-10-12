from django.shortcuts import render
from .models import all_posts, Post


# def get_date(post):
#   return post['date']

def home(request):
  # sorted_posts = all_posts
  # sorted_posts.sort(key=lambda post: post['date'])
  # latest_post = sorted_posts[-3:]

  latest_post = Post.objects.all().order_by('date')[:3]
  return render(request, 'blog/home.html', { 'posts': latest_post })


def list(request):
  posts = Post.objects.all()
  return render(request, 'blog/list.html', { 'posts': posts })


def detail(request, slug):
  choosen_post = Post.objects.get(slug=slug)
  choosen_tags = choosen_post.tag.all()
  # choosen = next(filter(lambda post:post['slug'] == slug, all_posts))
  # selected_post = next(post for post in all_posts if post['slug'] == slug)
  return render(request, 'blog/detail.html', { 'post': choosen_post, 'tags': choosen_tags })
