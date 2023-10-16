from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, View
from .utils import get_Object_or_none


class Home(CreateView):
    template_name = "reviews/home.html"
    model = Review
    fields = '__all__'
    success_url = 'thank'


class Favorite(View):
    def post(self, request):
        id = request.POST['review-id']
        request.session['id'] = id
        
        username = request.POST['review-user_name']
        return HttpResponseRedirect(username)


class Thank(TemplateView):
    template_name = 'reviews/thank.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = 'RAPHAEL'
        return context


class List(ListView):
    template_name = 'reviews/list.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        return super().get_queryset().filter(rating__gt=5)


class Detail(DetailView):
    template_name = 'reviews/single.html'
    model = Review
    context_object_name = 'review'

    def get_object(self):
        return Review.objects.get(user_name=self.kwargs.get("user_name"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        fav_id = self.request.session['id']
        loaded_object = self.object
        
        context["is_favorite"] = loaded_object.id == int(fav_id)
        return context
    
    

# class List(TemplateView):
#     template_name = 'reviews/list.html'
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['reviews'] = Review.objects.all()
#         return context


# class Detail(TemplateView):
#     template_name = 'reviews/single.html'

#     def get_context_data(self, *args, **kwargs):
#         # print(args, kwargs)
#         # id = kwargs['id']
#         context = super().get_context_data(**kwargs)
#         print(context)
#         context['review'] = get_Object_or_none(Review, user_name=context['id'])
#         return context


# class Home(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/home.html"

#     def form_valid(self, form: Any):
#         form.save()
#         return super().form_valid(form)

#     success_url = 'thank'


# class Home(View):

#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/home.html", {"form": form})

#     def post(self, request):
#         form = ReviewForm(request.POST)

#         existing_data = get_Object_or_none(Review, user_name=form.data['user_name'])
#         print(existing_data)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('thank')
#         return render(request, "reviews/home.html", {"form": form})


## WITHOUT FORMS
# def home(request):
#     if request.method == "POST":
#         username = request.POST['username']

#         if username == '' and len(username) < 3:
#             return render(request, 'reviews/home.html', {'has_error': True})

#         print(request.POST)
#         return HttpResponseRedirect('thank')
#     return render(request, 'reviews/home.html', {'has_error': False})


### WITH FORM AND SAVING REVIEW MODEL ONE-BY-ONE like updating
# def home(request):
#     if request.method == 'POST':

#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             # rev = Review(
#             #     user_name=form.cleaned_data['user_name'],
#             #     name=form.cleaned_data['name'],
#             #     email=form.cleaned_data['email'],
#             #     review_text=form.cleaned_data['review_text'],
#             #     rating=form.cleaned_data['rating']
#             # )
#             # rev.save()
#             form.save()
#             return HttpResponseRedirect('thank')
#     else:
#         form = ReviewForm()

#     return render(request, 'reviews/home.html', {'form': form})

# CLASS VIEW WITH GET AND POST
# class Home(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/home.html", {"form": form})
#
#     def post(self, request):
#         form = ReviewForm(request.POST)
#         try:
#             existing_data = Review.objects.get(user_name=form.data['user_name'])
#         except:
#             existing_data = None
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('thank')
#         return render(request, "reviews/home.html", {"form": form})



# class Thank(View):
#     def get(self, request):
#         return render(request, 'reviews/thank.html')
    

# def thank(request):
#     return render(request, 'reviews/thank.html')
