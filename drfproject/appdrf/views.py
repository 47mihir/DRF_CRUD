from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializer import PersonSerializer
from rest_framework import status
# Create your views here.



@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            user = Person.objects.get(id=id)
            serializer = PersonSerializer(user)
            return Response(serializer.data)
        user = Person.objects.all()
        serializer = PersonSerializer(user, many = True)
        return Response(serializer.data)
    

    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    if request.method == 'PUT':
        id=pk
        user = Person.objects.get(pk=id)
        serializer = PersonSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    if request.method == 'PATCH':
        id=pk
        user = Person.objects.get(pk=id)
        serializer = PersonSerializer(user, data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Partial Data Updated'})
        return Response(serializer.errors)


    if request.method == 'DELETE':
        id=pk
        user = Person.objects.get(pk=id)
        user.delete()
        return Response({'msg':'Data Deleted'})
