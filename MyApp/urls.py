from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:pk>/toggle/', views.task_toggle_status, name='task_toggle_status'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),

]

