from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='taskList'),
    path('task/<int:id>', views.taskView, name='taskView'),
    path('newtask/', views.newTask, name='newTask'),
    path('edittask/<int:id>', views.editTask, name='editTask'),
    path('deletetask/<int:id>', views.deleteTask, name='deleteTask'),
    path('changestatus/<int:id>', views.changeStatus, name='changeStatus'),
]