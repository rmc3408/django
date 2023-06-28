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
    
    context = { 'data': rooms }
    return render(request, 'home.html', context)


def room(request, id):
    # return render(request, 'room.html', { 'data': mockRooms[int(id)] })
    
    room = Room.objects.get(id=id)
    
    #print(room.__dict__)
    #pprint.pprint(room.__dict__, indent = 4)
    #print(model_to_dict(room))

    return render(request, 'room.html', { 'data': room })

