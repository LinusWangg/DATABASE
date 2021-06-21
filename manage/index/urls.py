"""treehole URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.primary_data,name=""),
    path('show',views.show_article,name="show"),
    path('dele',views.delete_article,name="dele"),
    path('1',views.primary_data2,name="1"),
    path('show_user',views.show_user,name="show_user"),
    path('dele_user',views.delete_user,name="dele_user"),
    path('2',views.primary_data3,name="2"),
    path('show_comment',views.show_comment,name="show_comment"),
    path('dele_comment',views.delete_comment,name="dele_comment"),
    path('3',views.primary_data4,name="3"),
    path('show_admin',views.show_admin,name="show_admin"),
    path('dele_admin',views.delete_admin,name="dele_admin"),
    path('add_admin',views.add_admin,name="add_admin"),
    path('give_admin',views.give_admin,name="give_admin"),
]