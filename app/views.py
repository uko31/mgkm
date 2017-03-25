from django.shortcuts import render
from django.http import HttpResponse

def AppIndex(request):
    return HttpResponse("This is juste a test")

def AppAdd(request, app_id):
    return HttpResponse("Add an App")

def AppEdit(request, app_id):
    return HttpResponse("Edit the App: " + app_id)

def AppDel(request, app_id):
    return HttpResponse("Del an App: " + app_id)
