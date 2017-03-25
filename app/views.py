from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import App

def index(request):
    action = ""
    if request.method == "POST":
        if ("action" and "ccx") in request.POST:
            action = "{} - {}".format(request.POST['action'], request.POST['ccx'])

    try:
        apps = App.objects.all()
    except:
        raise Http404("Oups!!")

    return render(request, "app/app_index.html", { 'apps': apps, 'action': action })

def add(request):
    return render(request, "app/app_form.html")

def edit(request, app_ccx):
    app = get_object_or_404(App, ccx = app_ccx.upper)

    return render(request, "app/app_form.html", { 'app': app })

def delete(request, app_ccx):
    app = get_object_or_404(App, ccx = app_ccx.upper)

    return render(request, "app/app_delete.html", { 'app': app })
