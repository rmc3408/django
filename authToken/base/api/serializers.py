from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from base.models import Note


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff' ]


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'