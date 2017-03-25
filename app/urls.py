from django.conf.urls import url

from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add/$', views.add, name="add"),
    url(r'^edit/(?P<app_ccx>[a-zA-Z0-9_]{3})$', views.edit, name="edit"),
    url(r'^del/(?P<app_ccx>[a-zA-Z0-9_]{3})$', views.delete, name="delete"),
]
