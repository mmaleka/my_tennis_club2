from django.urls import re_path, include
from . import views

app_name = 'api-serial_detection_api'


urlpatterns = [

    re_path('', views.Serial_DetectionAPIView.as_view(), name="serial_detection_api"),

]

