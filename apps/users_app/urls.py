from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^display/(?P<id>\d+)$', views.display),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^create$', views.create),
    url(r'^edit/update/(?P<id>\d+)$', views.update),
    url(r'^delete/(?P<id>\d+)$', views.delete),
]