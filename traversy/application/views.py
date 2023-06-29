from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import pprint
from django.forms.models import model_to_dict


def home(request):
  
    queryURL = request.GET.get('q') if (request.GET.get('q') != None) else ''
    
    rooms = Room.objects.filter(
        Q(topic__name__icontains=queryURL) |
        Q(name__icontains=queryURL) |
        Q(description__icontains=queryURL)
        )
    topics = Topic.objects.all()

    context = { 'data': rooms, 'topics': topics, 'totalRooms': rooms.count() }
    return render(request, 'home.html', context)


def room(request, id): 
    room = Room.objects.get(id=id)
    return render(request, 'room.html', { 'data': room })


@login_required(login_url='login')
def create(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = { 'form': form }
    return render(request, 'form_room.html', context)


@login_required(login_url='login')
def update(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = { 'form': form }
    return render(request, 'form_room.html', context)


@login_required(login_url='login')
def delete(request, id):
    room = Room.objects.get(id=id)

    if request.user != room.host:
        return HttpResponse('Your are not allowed here!!')
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
        
    context = { 'data': id }
    return render(request, 'delete.html', context)


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        userName = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            #user = User.objects.get(email=email)
            user = User.objects.get(username=userName)
        except:
            messages.error(request, 'User does not exist')

        userAuthenticated = authenticate(request, username=userName, password=password)
        
        print(userAuthenticated, user.email)

        if userAuthenticated is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password are wrong')

    context = { 'page': page }
    return render(request, 'login.html', context )


def logoutUser(request):
    logout(request)
    return redirect('home')