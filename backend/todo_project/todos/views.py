# todos/views.py
from rest_framework import generics
from rest_framework import routers, serializers, viewsets
from . import models
from . import serializers
from django.shortcuts import render





class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer

####ListLoginInfo
class ListLoginInfo(generics.ListCreateAPIView):
    queryset = models.LoginInfo.objects.all()
    serializer_class = serializers.LoginInfoSerializer
class DetailLoginInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.LoginInfo.objects.all()
    serializer_class = serializers.LoginInfoSerializer


######
class ListToDoList(generics.ListCreateAPIView):
    queryset = models.ToDoList.objects.all()
    serializer_class = serializers.ToDoListSerializer
class DetailToDoList(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ToDoList.objects.all()
    serializer_class = serializers.ToDoListSerializer


#####
class ListToDoListItem(generics.ListCreateAPIView):
    queryset = models.ToDoListItem.objects.all()
    serializer_class = serializers.ToDoListItemSerializer
class DetailToDoListItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ToDoListItem.objects.all()
    serializer_class = serializers.ToDoListItemSerializer



#####TR VIEWSET ILE
class User(viewsets.ModelViewSet):
    queryset = models.LoginInfo.objects.all()
    serializer_class = serializers.LoginInfoSerializer

class Lists(viewsets.ModelViewSet):
    queryset = models.ToDoList.objects.all()
    serializer_class = serializers.ToDoListSerializer

class Items(viewsets.ModelViewSet):
    queryset = models.ToDoListItem.objects.all()
    serializer_class = serializers.ToDoListItemSerializer




#####new style;
