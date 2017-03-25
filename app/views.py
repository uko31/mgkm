from django.shortcuts import render
from django.http import HttpResponse

def AppIndex(request):
    return HttpResponse("Application index view")

def AppAdd(request):
    return HttpResponse("Add an App")

def AppEdit(request, app_id):
    return HttpResponse("Edit the App: " + app_id)

def AppDel(request, app_id):
    return HttpResponse("Del an App: " + app_id)
