from rest_framework import serializers
from .models import Park

class PlateInputSerializer(serializers.Serializer):
    carno=serializers.CharField(max_length=11)

class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        slot = serializers.IntegerField()
        carno = serializers.CharField(max_length=11)
        model= Park
        fields = "__all__"
