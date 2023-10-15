from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView
from django.http import HttpResponseRedirect
from .forms import ProfileFileForm
from .models import Profile

# Create your views here.

class CreateProfileView(View):
    def get(self, request):
        form = ProfileFileForm()
        return render(request, "profiles/create_profile.html", { 'form': form })

    def post(self,request):
        form = ProfileFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            profileUser = Profile(image=request.FILES['image'], text=request.FILES['text'])
            profileUser.save()
            return HttpResponseRedirect('/profiles/')
    
    # def post(self, request):
    #     store_uploaded_file(request.FILES['image'])
    #     return HttpResponseRedirect('/profiles/')


class CreateProfile(CreateView):
    template_name = 'profiles/create_profile.html'
    model = Profile
    fields = '__all__'
    success_url = '/profiles/'


class ListProfile(ListView):
    model = Profile
    template_name = 'profiles/read_profile.html'
    