from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^en/contact/', views.contact, name='contact'),
    url(r'^en/services/', views.services, name='services'),
    url(r'^en/architecture/', views.architecture, name='architecture'),
    url(r'^en/design/', views.design, name='design'),
    url(r'^ru/home/', views.ruindex, name='ruindex'),
    url(r'^ru/contact/', views.rucontact, name='rucontact'),
    url(r'^ru/services/', views.ruservices, name='ruservices'),
    url(r'^ru/architecture/', views.ruarchitecture, name='ruarchitecture'),
    url(r'^ru/design/', views.rudesign, name='rudesign'),
    ]
