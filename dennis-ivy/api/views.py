from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .tests import mockRoutes
from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def getRoutes(request):
    return Response(mockRoutes)


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all().order_by('-updatedAt')
    serialized_Notes = NoteSerializer(notes, many=True)
    return Response(serialized_Notes.data)


@api_view(['GET'])
def getNote(request, id):
    note = Note.objects.get(id=id)
    serialized_Note = NoteSerializer(note, many=False)
    return Response(serialized_Note.data)


@api_view(['PUT'])
def updateNote(request, id):
    data = request.data
    note = Note.objects.get(id=id)
    serialized_Note = NoteSerializer(instance=note, data=data)

    if serialized_Note.is_valid():
        serialized_Note.save()
    
    return Response(serialized_Note.data)


@api_view(['DELETE'])
def deleteNote(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return Response('deleted {{id}}')


@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(body=data['body'])
    serialized_Note = NoteSerializer(instance=note, many=False)
    return Response(serialized_Note.data)

