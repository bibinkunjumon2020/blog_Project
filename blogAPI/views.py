from django.shortcuts import render
from django.db import models
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from blogAPI.models import Mobiles
from blogAPI.serializers import MobileSerializers

class MobileView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        serializer=MobileSerializers(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=MobileSerializers(data=request.data)
        '''Mobiles.objects.create(name=serializer.initial_data.get("name"),price=serializer.initial_data.get("price"),
                               band=serializer.initial_data.get("band"),
                               display=serializer.initial_data.get("display"),
                               processor=serializer.initial_data.get("processor"),)'''
        Mobiles.objects.create(**serializer.initial_data)

        # if serializer.is_valid():
          #  Mobiles.objects.create(**serializer.validated_data)
        return Response(data=request.data)

