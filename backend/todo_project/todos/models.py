# todos/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#well, lets create some models for huawei


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title

class LoginInfo(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    create_date = models.DateField(default=timezone.now)
    edited_date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.user

class ToDoList(models.Model):
     todolist_owner_id=models.ForeignKey(LoginInfo, on_delete=models.CASCADE)
     todolist_name=models.TextField(max_length=100)
     todolist_due_date=models.DateField()
     todolist_status=models.BooleanField(default=False)

class ToDoListItem(models.Model):
    todolist_id=models.ForeignKey(ToDoList , on_delete=models.CASCADE)
    todolistitem_owner=models.CharField(max_length=100)
    todolistitem_name=models.CharField(max_length=100)
    todolistitem_status=models.BooleanField(default=False)
    todolistitem_deadline=models.DateField()
    todolistitem_description=models.TextField()
    todolistitem_createdate=models.DateField()
    todolistitem_updatedate=models.DateField()


