from django.contrib import admin

from .models import Todo
from .models import LoginInfo
from .models import ToDoList
from .models import ToDoListItem


admin.site.register(Todo)
admin.site.register(LoginInfo)
admin.site.register(ToDoList)
admin.site.register(ToDoListItem)