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
    notes = Note.objects.all()
    serialized_Notes = NoteSerializer(notes, many=True)
    return Response(serialized_Notes.data)


@api_view(['GET'])
def getNote(request, id):
    note = Note.objects.get(id=id)
    serialized_Note = NoteSerializer(note, many=False)
    return Response(serialized_Note.data)