from ast import Not
from functools import partial
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from appdjango import serializers
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def person_api(request):
    if request.method == 'GET':     #get_data()
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            user = Person.objects.get(id=id)
            serializer = PersonSerializer(user)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        user = Person.objects.all()
        serializer = PersonSerializer(user, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')


    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = PersonSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        user = Person.objects.get(id=id)
        print(user)
        serializer = PersonSerializer(user, data = pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            res = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        user = Person.objects.get(id=id)
        user.delete()
        res = {'msg': 'Data Deleted'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res, safe=False)
       