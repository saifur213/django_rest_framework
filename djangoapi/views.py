from django.shortcuts import render
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

#function based api view
from rest_framework.decorators import api_view
#class based api view
from rest_framework.views import APIView
from rest_framework.response import Response

#List model mixin
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

#List create api view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

#Model View Set
from rest_framework import viewsets

#Authentication -- general user not allow to view / onley is staff and supper user allow
from rest_framework.permissions import IsAdminUser

# Create your views here.
#Queryset
def teacher_infos(request):
    #complex data
    t = Teacher.objects.all()
    #python dictionary
    serializer = TeacherSerializer(t,many=True)
    #render json
    json_data = JSONRenderer().render(serializer.data)
    #json sent to user
    return HttpResponse(json_data,content_type='application/json')


#Model Instance
def teacher_info(request,pk):
    #complex data
    t = Teacher.objects.get(id=pk)
    #python dictionary
    serializer = TeacherSerializer(t)
    #render json
    json_data = JSONRenderer().render(serializer.data)
    #json sent to user
    return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def teacher_create(request):
    if request.method == 'POST':
        json_data = request.body
        #json to stream convert
        stream = io.BytesIO(json_data)
        #stream to python
        pythondata = JSONParser().parse(stream)
        #pythoon to complex data
        serializer = TeacherSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Successfully insert data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application.json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application.json')
    
    if request.method == 'PUT':
        json_data = request.body
        #json to stream
        stream = io.BytesIO(json_data)
        #stream to python
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        teacher = Teacher.objects.get(id=id)
        #partial update
        #serializer = TeacherSerializer(teacher, data=pythondata, partial=True)
        #Full Update
        serializer = TeacherSerializer(teacher, data=pythondata)
        if serializer.is_valid():
            # serializer.update(instance,validated_data)
            serializer.save()
            res = {'msg': 'Successfully update data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application.json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application.json')
    
    if request.method == 'DELETE':
        json_data = request.body
        #json to stream
        stream = io.BytesIO(json_data)
        #stream to python
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        res = {'msg': 'Successfully update data'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='applicatioon.json')
    
#GET and POST method using API view
@api_view(['GET','POST', 'PUT', 'PATCH', 'DELETE'])
def teacher_create_api(request,pk=None):
    #Get data
    if request.method == 'GET':
        id = pk
        if id is not None:
            # complex data
            t = Teacher.objects.get(id=id)
            #convert python dictionary
            serializer = TeacherSerializer(t)
            return Response(serializer.data)
        #complex data
        t = Teacher.objects.all()
        #convert python dictionary
        serializer = TeacherSerializer(t,many=True)
        return Response(serializer.data)
    
    #Insert Data
    if request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Successfully Insert Data'}
            return Response(res)
        return Response(serializer.errors)
    
    #partial update
    if request.method == "PUT":
        id = pk
        t = Teacher.objects.get(pk=id)
        serializer = TeacherSerializer(t, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Successfuly update full data'})
        return Response(serializer.errors)
    
    #Full update
    if request.method == "PATCH":
        id = pk
        t = Teacher.objects.get(pk=id)
        serializer = TeacherSerializer(t, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Successfuly update partial data'})
        return Response(serializer.errors)
    
    #Delete data
    if request.method == "DELETE":
        id = pk
        t = Teacher.objects.get(pk=id)
        t.delete()
   
        return Response({'msg':'Successfuly delete data'})
        
    
#Class based view
class teacher_create_class_based_api_view(APIView):
    #Get data
    def get(self, request, pk=None, formate=None):
        id = pk
        if id is not None:
            # complex data
            t = Teacher.objects.get(id=id)
            #convert python dictionary
            serializer = TeacherSerializer(t)
            return Response(serializer.data)
        #complex data
        t = Teacher.objects.all()
        #convert python dictionary
        serializer = TeacherSerializer(t,many=True)
        return Response(serializer.data)
    
    #Insert Data
    def post(self, request, formate=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Successfully Insert Data'}
            return Response(res)
        return Response(serializer.errors)
    
    #partial update
    def put(self, request, pk, formate=None):
        id = pk
        t = Teacher.objects.get(pk=id)
        serializer = TeacherSerializer(t, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Successfuly update full data'})
        return Response(serializer.errors)
    
    #Full update
    def patch(self, request, pk, formate=None):
        id = pk
        t = Teacher.objects.get(pk=id)
        serializer = TeacherSerializer(t, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Successfuly update partial data'})
        return Response(serializer.errors)
    
    #Delete data
    def delete(self, request, pk, formate=None):
        id = pk
        t = Teacher.objects.get(pk=id)
        t.delete()
   
        return Response({'msg':'Successfuly delete data'})

#list model mixin
class teacherListCreate(GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    #show all teacher
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    #creat new teacher
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class teacherListRetrieveUpdateDelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    # show specific teacher instant
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    # update specific teacher instant
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    # delete specific teacher instant
    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)  


#List create api view
class teacherListCreateApiView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class teacherListApiViewRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

#Model View Set
class teacherModelViewSet(viewsets.ModelViewSet):
    #List, create, delete, update, partial update
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    #Authentication -- general user not allow to view / onley is staff and supper user allow
    permission_classes = [IsAdminUser]

    