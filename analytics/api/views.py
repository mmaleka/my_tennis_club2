from rest_framework import generics, mixins
from rest_framework.views import APIView
import datetime
import cv2

import requests


from analytics.models import pingservor
from . serializers import pingservorSerializers


class pingservorList(generics.ListAPIView):
    queryset = pingservor.objects.all()
    serializer_class = pingservorSerializers


class pingservorPost(generics.CreateAPIView):
    serializer_class = pingservorSerializers


# class ScannerDataSerilisersAPIView(
#     mixins.CreateModelMixin,
#     generics.ListAPIView,
#     ):


#     lookup_field = 'id'
#     serializer_class =  ScannerDataDataSerialisersv1


#     def get_queryset(self):
#         today = datetime.datetime.now().date()
#         return ScannerData.objects.filter(
#             created_at__gte=today)

#     def post(self, request, *args, **kwargs):
#         serializer = ScannerDataDataSerialisersv1(data=request.data)
#         if serializer.is_valid():
#             self.post_server(
#                 serializer.data['shell_no'],
#                 serializer.data['cast_code'],
#                 serializer.data['heat_code'],
#                 serializer.data['shell_serial_no'],
#                 serializer.data['location'])
#         return self.create(request, *args, **kwargs)
