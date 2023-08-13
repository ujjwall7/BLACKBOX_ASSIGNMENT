from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('upload-json/', UploadJsonView.as_view(), name='upload_json'),
]