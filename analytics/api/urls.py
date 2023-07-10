from django.urls import path
from . import views

app_name = 'api-pingservor'

urlpatterns = [

     path('pingservorList/', 
          views.pingservorList.as_view(), 
          name='pingservorList'),

     path('pingservorPost/', 
          views.pingservorPost.as_view(), 
          name='pingservorPost'),
    
]