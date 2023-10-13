from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from .utils import get_Object_or_none

class Home(View):

    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/home.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)


        existing_data = get_Object_or_none(Review, user_name=form.data['user_name'])
        print(existing_data)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thank')
        return render(request, "reviews/home.html", {"form": form})


class Thank(TemplateView):
    template_name = 'reviews/thank.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = 'RAPHAEL'
        return context


class ReviewList(TemplateView):
    template_name = 'reviews/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        return context


class Detail(TemplateView):
    template_name = 'reviews/single.html'

    def get_context_data(self, *args, **kwargs):
        # print(args, kwargs)
        # id = kwargs['id']
        context = super().get_context_data(**kwargs)
        print(context)
        context['review'] = get_Object_or_none(Review, user_name=context['id'])
        return context


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
