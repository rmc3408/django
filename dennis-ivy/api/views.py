from django.shortcuts import render
from django.http import JsonResponse
from .tests import mockRoutes

def getRoutes(request):
    return JsonResponse(mockRoutes, safe=False)

