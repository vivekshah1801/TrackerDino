from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.view),
    path("create", views.create), # POST 
    path("details/<str:tracker>", views.details), # GET
    path("delete/<str:tracker>", views.delete), # DELETE
    path("toggle/<str:tracker>", views.toggle), # PUT
    path("toggle_notif/<str:tracker>", views.toggle_notif), # PUT
]
