from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
from django.views import View

# def home(request):
#     if request.method == "POST":
#         username = request.POST['username']

#         if username == '' and len(username) < 3:
#             return render(request, 'reviews/home.html', {'has_error': True})

#         print(request.POST)
#         return HttpResponseRedirect('thank')
#     return render(request, 'reviews/home.html', {'has_error': False})


# def home(request):
#     if request.method == 'POST':

#         form = ReviewForm(request.POST)

#         existing_data = Review.objects.get(user_name=form.data['user_name'])
#         if existing_data:
#             pass # update data

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


class Home(View):

    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/home.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)

        try:
            existing_data = Review.objects.get(user_name=form.data['user_name'])
        except:
            existing_data = None

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thank')
        return render(request, "reviews/home.html", {"form": form})


def thank(request):
    return render(request, 'reviews/thank.html')
