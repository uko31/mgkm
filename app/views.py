from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import App

def AppIndex(request):
    try:
        apps = App.objects.all()
        html = "Application List:<br><ul>"
        for app in apps:
            html += "<li><a href='/app/edit/{}'>{}</a> (<a href='/app/del/{}'>delete</a>)</li>".format(app.ccx, app.ccx, app.ccx)
        html += "</ul>"
    except:
        raise Http404("Oups!!")

    return HttpResponse(html)

def AppAdd(request):
    return HttpResponse("Add an App")

def AppEdit(request, app_ccx):
    try:
        app_ccx = app_ccx.upper()
        app = App.objects.get(ccx = app_ccx)
    except:
        raise Http404("the application '{}' does not exists!".format(app_ccx))

    return HttpResponse("Edit the App: " + app_ccx)

def AppDel(request, app_ccx):
    return HttpResponse("Are you sure you want to delete the {} application ?".format(app_ccx))
