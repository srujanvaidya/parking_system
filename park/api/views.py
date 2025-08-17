from gc import get_objects

from django.http import Http404
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,mixins
from .serializers import PlateSerializer,PlateInputSerializer
from .models import Park
from .sqltest import Server
from .parking import Parkings


class Parkingsys(APIView):

    def get(self,request):
        park=Park.objects.all()
        serializer=PlateSerializer(park,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Parks(APIView):



    def post(self,request):
        serializer= PlateInputSerializer(data=request.data)
        if serializer.is_valid():
            p=Parkings()
            data=request.data
            plate=data['carno']
            p.park(plate)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Exit(APIView):



    def post(self,request):
        serializer=PlateInputSerializer(data=request.data)
        if serializer.is_valid():
            p=Parkings()
            data=request.data
            plate=data['carno']
            p.depart(plate)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






















