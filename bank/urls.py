# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    
    path('view', views.index, name='viewCustomer'),
    path('Registeration', views.Registeration, name='Registeration'),
    path('', views.Home, name='Home'),
    path('transfer/<str:username>', views.transfer, name='transfer')
    
    
]

