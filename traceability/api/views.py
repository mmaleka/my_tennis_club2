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
        added = self.request.query_params.get('added')
        if added:
            return ScannerData.objects.filter(
                created_at__gte=today,
                added=added)
        else:
            return ScannerData.objects.filter(
                created_at__gte=today)

    def post(self, request, *args, **kwargs):
        serializer = ScannerDataDataSerialisersv1(data=request.data)

        return self.create(request, *args, **kwargs)



class ScannerDataSerilisersDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = ScannerData.objects.all()
    lookup_field = 'id'
    serializer_class = ScannerDataDataSerialisersv1

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)