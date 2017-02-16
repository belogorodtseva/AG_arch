from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^services/', views.services, name='services'),
    url(r'^architecture/', views.architecture, name='architecture'),
    url(r'^design/', views.design, name='design'),
    ]
