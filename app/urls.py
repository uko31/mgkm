from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AppIndex, name="app_index"),
]
