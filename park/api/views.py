from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,mixins
from .serializers import PlateSerializer,Plate1Serializer
from .models import Park
from .sqltest import Server
from .parking import Parkings


class Parkingsys(APIView):
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

    def post(self,request):
        serializer=Plate1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            p = Parkings()
            data=request.data
            plateno=data['plate']
            #print(plateno)
            p.park(plateno)
            return Response(serializer.data,status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)














