from django.urls import path, include

from .views import *

urlpatterns = [
    path('', compress_image, name='home'),    
]
