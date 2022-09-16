from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from productsapi.serializer_my import MySerializer,ModelSerializer,UserSerializer
from productsapi.models import ProductItems
from rest_framework import status,authentication,permissions
from django.contrib.auth.models import User
# Create your views here.

## We used NORMAL SERIALIZER IN THE FOLLOWING CODE
class ProductView(APIView):
    def get(self,request,*args,**kwargs): # accessing all details
        try:
            data=ProductItems.objects.all()
            my_serializer=MySerializer(data,many=True)
            return Response(data=my_serializer.data)
        except:
            return Response({"msg":"Error in get"},status=status.HTTP_404_NOT_FOUND)
    def post(self,request,*args,**kwargs): #inserting fields
        #print(request.data)
        my_serializer=MySerializer(data=request.data)
       # print(my_serializer.initial_data)
        ProductItems.objects.create(**my_serializer.initial_data)
        return Response(data=request.data)

class ProductListView(APIView):
    def get(self,request,*args,**kwargs): #returning values with specific id
        id = kwargs.get("id")
        try:
            data = ProductItems.objects.get(id=id)
            my_serializer = MySerializer(data)
            return Response(data=my_serializer.data)
        except:
            return Response({"msg": "Error in get"},status=status.HTTP_404_NOT_FOUND)
    def put(self,request,*args,**kwargs): # Updating Content
        id=kwargs.get("id")
        try:
            data_db=ProductItems.objects.get(id=id)
            my_serialize=MySerializer(data=request.data)
            if my_serialize.is_valid():
                data_db.title=my_serialize.validated_data.get("title")
                data_db.price = my_serialize.validated_data.get("price")
                data_db.rating = my_serialize.validated_data.get("rating")
                data_db.category = my_serialize.validated_data.get("category")
                data_db.description = my_serialize.validated_data.get("description")
                data_db.save()
            return Response(my_serialize.data)
        except:
            return Response({"msg": "Error in Put"},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,*args,**kwargs): # Deleting the field
        id = kwargs.get("id")
        try:
            data_from_db=ProductItems.objects.get(id=id)
            data_from_db.delete()
            return Response(request.data)
        except:
            return Response({"msg": "Error in delete"},status=status.HTTP_404_NOT_FOUND)

# We used MODEL SERIALIZER IN THE FOLLOWING CODE
class ProductViewModelSerialView(APIView):
    def get(self,request,*args,**kwargs):
        data = ProductItems.objects.all()
        serializer_model = ModelSerializer(data,many=True)
        return Response(data=serializer_model.data)
    def post(self,request,*args,**kwargs):
        serializer = ModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ProductViewModelListView(APIView):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        data = ProductItems.objects.get(id=id)
        serializer_model = ModelSerializer(data)
        return Response(data=serializer_model.data)
    def delete(self,request,*args,**kwargs):
        id = kwargs.get("id")
        data = ProductItems.objects.get(id=id)
        data.delete()
        return Response({"msg":"Item deleted"})
    def put(self,request,*args,**kwargs):
        id = kwargs.get("id")
        data_obj = ProductItems.objects.get(id=id)
        serializer_model = ModelSerializer(data=request.data,instance=data_obj) # only difference with create in this line the instance varibale
        if serializer_model.is_valid():
            serializer_model.save()
            return Response(data=serializer_model.data)
        else:
            return Response(data=serializer_model.errors)

# We used MODEL SERIALIZER & VIEW SET FUNCTIONS IN THE FOLLOWING CODE

class ProductViewSetView(viewsets.ViewSet):
    def list(self,request,*args,**kwargs):
        qs = ProductItems.objects.all()
        serializer = ModelSerializer(instance=qs,many=True) # To deserialise we use 'instance'
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def create(self,request,*args,**kwargs):
        serializer = ModelSerializer(data=request.data) # to serialise we use 'data'
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.initial_data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        object = ProductItems.objects.get(id=id)
        serializer=ModelSerializer(object)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def update(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        object = ProductItems.objects.get(id=id)
        serializer = ModelSerializer(data=request.data,instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        object = ProductItems.objects.get(id=id)
        object.delete()
        return Response({"msg":"Deleted"},status=status.HTTP_204_NO_CONTENT)

# All the above mentioned methods are in built in modelviewset class
class ProductModelViewSetView(viewsets.ModelViewSet):
    # checking authentication
    #authentication_classes = [authentication.BasicAuthentication]
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    # using model serialiser
    serializer_class = ModelSerializer
    queryset = ProductItems.objects.all()


class UserRegistrationView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
