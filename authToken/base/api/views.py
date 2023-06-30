from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from .serializers import UserSerializer, NoteSerializer
from rest_framework.decorators import api_view, permission_classes
#from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from base.models import Note


@api_view(['GET'])
def getRouters(request):
    routes = [ '/token', '/token/refresh' ]
    return Response(routes)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


class UserViewSet(RetrieveAPIView):    
    
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
