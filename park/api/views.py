from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,mixins
from .serializers import PlateSerializer
from .models import Park
from .sql_test import Server

class Parking(APIView):
    def obj(self):
        server = Server()
        raw = server.find()
        final = [
            {"id": row[0], "plate": row[1]} for row in raw
        ]
        return final
    def get(self,request):
        data=self.obj()
        serializer = PlateSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)





