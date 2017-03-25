from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AppIndex, name="app_index"),
    url(r'^add/$', views.AppAdd, name="app_add"),
    url(r'^edit/(?P<app_ccx>[a-zA-Z0-9_]{3})$', views.AppEdit, name="app_edit"),
    url(r'^del/(?P<app_ccx>[a-zA-Z0-9_]{3})$', views.AppDel, name="app_del"),
]
