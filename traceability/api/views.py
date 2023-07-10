from rest_framework import generics, mixins
from rest_framework.views import APIView
import datetime

import requests



from traceability.models import traceability, ScannerData
from . serializers import traceabilitySerializers, ScannerDataDataSerialisersv1


class traceabilityList(generics.ListAPIView):
    queryset = traceability.objects.all()
    serializer_class = traceabilitySerializers


class traceabilityPost(generics.CreateAPIView):
    serializer_class = traceabilitySerializers



class ScannerDataSerilisersAPIView(
    mixins.CreateModelMixin, 
    generics.ListAPIView,
    ):


    lookup_field = 'id'
    serializer_class =  ScannerDataDataSerialisersv1


    def get_queryset(self):
        today = datetime.datetime.now().date()
        return ScannerData.objects.filter(
            created_at__gte=today)

    def post(self, request, *args, **kwargs):
        serializer = ScannerDataDataSerialisersv1(data=request.data)

        return self.create(request, *args, **kwargs)