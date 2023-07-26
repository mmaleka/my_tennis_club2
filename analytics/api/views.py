from rest_framework import generics, mixins
from rest_framework.views import APIView
import datetime
from datetime import datetime, timedelta, time


from analytics.models import pingservor
from . serializers import pingservorSerializers


class pingservorList(generics.ListAPIView):

    serializer_class = pingservorSerializers

    def get_queryset(self):
        ping_server = self.request.query_params.get('ping_server')
        today = datetime.now().date() - timedelta(1)
        queryset = pingservor.objects.filter(
            created__gte=today,
            ping_server__contains=ping_server
        )

        return queryset


class pingservorPost(generics.CreateAPIView):
    serializer_class = pingservorSerializers


