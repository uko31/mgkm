from django.shortcuts import render
from django.http import HttpResponse

def AppIndex(request):
    return HttpResponse("This is juste a test")
