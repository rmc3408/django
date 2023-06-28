from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    #host = models.CharField()
    #topic = models.TextField()
    name = models.CharField(max_length=52)
    description = models.TextField(null=True, blank=True)
    #participants = 
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=52)

    def __str__(self):
        return self.name
    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.body[0:31]


