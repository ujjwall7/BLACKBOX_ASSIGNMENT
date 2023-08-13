from django.contrib import admin
from django.urls import path
from .views import *
from .import views 

urlpatterns = [
    path('upload-json/', UploadJsonView.as_view(), name='upload_json'),
    path('', views.dashboard, name='dashboard'),
]