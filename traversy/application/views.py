from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm
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


def create(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = { 'form': form }
    return render(request, 'form_room.html', context)


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


def delete(request, id):
    room = Room.objects.get(id=id)

    if request.method == 'POST':
        room.delete()
        return redirect('home')
        
    context = { 'data': id }
    return render(request, 'delete.html', context)

