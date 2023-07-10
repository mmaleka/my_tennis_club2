from rest_framework import serializers
from analytics.models import pingservor




class pingservorSerializers(serializers.ModelSerializer):

    class Meta:
        model = pingservor
        fields = '__all__'






