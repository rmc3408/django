from django.shortcuts import render
from .models import Post
from .forms import CommentForm
from django.views.generic import ListView, DetailView, View
from django.http import HttpResponseRedirect
from django.urls import reverse


class Home(ListView):
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    model = Post

    def get_queryset(self):
        return super().get_queryset().order_by('date')[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class List(ListView):
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReadLaterView(View):
    


    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)

    def post(self, request):

        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")


class Detail(DetailView):
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    model = Post

    def is_stored_post(self, post_id):
        stored_posts = self.request.session.get('stored_posts')
        if stored_posts is not None and post_id in stored_posts:
            return True
        else:
            return False

    def get_context_data(self, **kwargs):
        detailed_post = self.get_object()
        context = super().get_context_data(**kwargs)

        context['later'] = self.is_stored_post(detailed_post.id) # type: ignore
        context['tags'] = detailed_post.tag.all()  # type: ignore
        context['comment_form'] = CommentForm()
        context['comments'] = detailed_post.comments.all()  # type: ignore
        # print(context)
        return context

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("detail_page", args=[slug]))

        else:
            context = {
                "post": post,
                "post_tags": post.tag.all(),
                "comment_form": comment_form,
                "comments": post.comments.all().order_by("-id"),  # type: ignore
                "later": self.is_stored_post(post.id)  # type: ignore
            }
            return render(request, "blog/detail.html", context)

    # def get(self, request, slug):
    #     post = Post.objects.get(slug=slug)

    #     context = {
    #         "post": post,
    #         "post_tags": post.tag.all(),
    #         "comment_form": CommentForm(),
    #         "comments": post.comments.all().order_by("-id"),
    #     }
    #     return render(request, "blog/detail.html", context)


# FUNCTIONS VIEWS

# def home(request):
#     # sorted_posts = all_posts
#     # sorted_posts.sort(key=lambda post: post['date'])
#     # latest_post = sorted_posts[-3:]
#     latest_post = Post.objects.all().order_by('date')[:3]
#     return render(request, 'blog/home.html', {'posts': latest_post})

# def list(request):
#   posts = Post.objects.all()
#   return render(request, 'blog/list.html', { 'posts': posts })

# def detail(request, slug):
#     choosen_post = Post.objects.get(slug=slug)
#     choosen_tags = choosen_post.tag.all()
#     # choosen = next(filter(lambda post:post['slug'] == slug, all_posts))
#     # selected_post = next(post for post in all_posts if post['slug'] == slug)
#     return render(request, 'blog/detail.html', {'post': choosen_post, 'tags': choosen_tags})
