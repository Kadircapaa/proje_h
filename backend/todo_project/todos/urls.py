# todos/urls.py
from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('User',views.User)
router.register('Lists',views.Lists)
router.register('Items',views.Items)


urlpatterns = [
  #  path('', views.ListTodo.as_view()),
    path('',include(router.urls)),
  #  path('/leads/', include('views.LeadListCreate.urls')),


    #path('test/<int:pk>/', views.DetailTodo.as_view()),


      #path('login/list/<int:pk>/', views.ListLoginInfo.as_view()),
     #  path('login/detail/<int:pk>/', views.DetailLoginInfo.as_view()),
    

    #   path('todolist/list/<int:pk>/', views.ListToDoList.as_view()),
    #   path('todolist/detail/<int:pk>/', views.DetailToDoList.as_view()),

     #  path('itemtodolist/list/<int:pk>/', views.ListToDoListItem.as_view()),
    #   path('itemtodolist/detail/<int:pk>/', views.DetailToDoListItem.as_view()),

]