from rest_framework import serializers
from .models import Park

class PlateSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    plate=serializers.CharField(max_length=11)
