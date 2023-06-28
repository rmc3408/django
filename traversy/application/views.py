from django.shortcuts import render
# from django.http import HttpResponse

rooms = [
    { 'id': 1, 'name': 'python'},
    { 'id': 2, 'name': 'node'},
    { 'id': 3, 'name': 'java'},
]


def home(request):
    # return HttpResponse('Home page')
    return render(request, 'application/home.html', { 'data': rooms })


def room(request):
    return render(request, 'application/room.html')

