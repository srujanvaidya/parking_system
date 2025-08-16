from rest_framework import serializers
from .models import Park

class PlateSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    plate=serializers.CharField(max_length=11)

class Plate1Serializer(serializers.ModelSerializer):
    class Meta:
        model= Park
        fields = "__all__"
