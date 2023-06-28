from django.shortcuts import render
# from django.http import HttpResponse
from .models import Room

import pprint
from django.forms.models import model_to_dict

# mockRooms = [
#     { 'id': 0, 'name': 'python'},
#     { 'id': 1, 'name': 'node'},
#     { 'id': 2, 'name': 'java'},
# ]



def home(request):
    # return HttpResponse('Home page')
    # return render(request, 'home.html', { 'data': mockRooms })
    
    rooms = Room.objects.all()
    # for i in rooms:
    #     print(model_to_dict(i))

    context = { 'data': rooms }
    return render(request, 'home.html', context)


def room(request, id):
    # return render(request, 'room.html', { 'data': mockRooms[int(id)] })
    
    room = Room.objects.get(id=id)
    #pprint.pprint(room.__dict__, indent = 4)
    #print(room.__dict__)
    #print(model_to_dict(room))

    return render(request, 'room.html', { 'data': room })


def form(request, id):
    room = Room.objects.get(id=id)

    context = { 'data': room }
    return render(request, 'form_room.html', context )
