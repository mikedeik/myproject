from django.shortcuts import render , HttpResponse
from .models import Person, Bidder, Seller, Category, Item
from .serializers import PersonSerializer, UserSerializer, CategorySerializer , BidderSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import  APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# Create your views here.


def Index(request):
    return HttpResponse("Hello there!")

# class PersonViewSet(viewsets.ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer


''' GENERICS AND MIXINS'''


class PersonList(generics.GenericAPIView , mixins.ListModelMixin ,mixins.CreateModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)


class PersonDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    lookup_field = 'id'

    def get(self ,request ,id):
        return self.retrieve(request , id = id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self , request , id):
        return  self.destroy(request , id = id)


''' USer views'''


class UserList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [AllowAny]
    # authentication_classes = (TokenAuthentication,)

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class UserDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)

    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)


class CategoryList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'CategoryId'

    def get(self, request):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)


class CategoryHandle(generics.GenericAPIView, mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    lookup_field = 'CategoryId'

    def get(self, request, CategoryId):
        return self.retrieve(request , CategoryId = CategoryId)

    def put(self, request, CategoryId):
        return self.update(request, CategoryId = CategoryId)

    def delete(self, request , CategoryId):
        return self.destroy(request, CategoryId=CategoryId)


class BidderList(generics.GenericAPIView , mixins.ListModelMixin ,mixins.CreateModelMixin):
    queryset = Bidder.objects.all()
    serializer_class = BidderSerializer
    # permission_classes = [AllowAny]
    # authentication_classes = (TokenAuthentication,)

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)




'''
# CLASS VIEW

class PersonList(APIView):

    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons , many= True)
        return Response(serializer.data)

    def post(self , request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)


class PersonDetails(APIView):
    def get_object(self , id):
        try:
            return Person.objects.get(id = id)

        except Person.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)

    def get(self, request , id):
        person = self.get_object(id)
        serializer = PersonSerializer(person)
        return Response(serializer.data)


    def put(self , request ,id):
        person = self.get_object(id)
        serializer = PersonSerializer(person ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request , id):
        person = self.get_object(id)
        person.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

'''
'''
# API VIEW


# # den prepei na gine
# # @csrf_exempt # den prepei na ginei auto (mono gia post requests apo anauthorized users (postman) )
#
# @api_view(['GET','POST'])
# def person_list(request):
#     # get all persons
#     if request.method == 'GET':
#         persons = Person.objects.all()
#         serializer = PersonSerializer(persons , many= True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#
#         serializer = PersonSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#     return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
#
#
#
# @api_view(['GET','PUT','DELETE'])
# def person_details(request,pk):
#
#     try:
#         person = Person.objects.get(pk = pk)
#
#     except Person.DoesNotExist:
#         return Response(status= status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = PersonSerializer(person)
#         return  Response(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = PersonSerializer(person , data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         person.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
#

'''
