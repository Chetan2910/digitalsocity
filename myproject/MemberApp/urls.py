"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('m_all_members/',views.m_all_members, name="m_all_members"),
    path('m-profile/', views.m_profile, name="m-profile"),    
    path('m_add_member/',views.m_add_member, name='m_add_member'),
    path('m-all-notice/', views.m_all_notice, name='m-all-notice'),
    path('m-all-notice-details/<int:pk>', views.m_all_notice_details, name='m-all-notice-details'),
    path('m-all-event/', views.m_all_event, name='m-all-event'),
    path('m-all-event-details/<int:pk>', views.m_all_event_details, name='m-all-event-details'),
    path('m-add-event/', views.m_add_event, name='m-add-event'),

 
]
