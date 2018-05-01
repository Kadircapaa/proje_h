# todos/serializers.py
from rest_framework import serializers
from . import models
from .models import LoginInfo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Todo


class LoginInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
           # 'id',
            'user',
            'password',
            'email',
            'create_date',
            'edited_date',
        )
        model = models.LoginInfo


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'todolist_owner_id',
            'todolist_name',
            'todolist_due_date',
            'todolist_status',
        )
        model = models.ToDoList




class ToDoListItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'todolist_id',
            'todolistitem_owner',
            'todolistitem_name',
            'todolistitem_status',
            'todolistitem_deadline',
            'todolistitem_description',
            'todolistitem_createdate',
            'todolistitem_updatedate',

        )
        model = models.ToDoListItem


#################################

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Todo

