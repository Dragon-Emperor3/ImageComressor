from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home, name='home'),    
    path('show', show, name='show'),    
    path('download', download, name='download'),    
]
