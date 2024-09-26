from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/complete/', views.mark_completed, name='mark_completed'),
    path('tasks/<int:pk>/not_started/', views.mark_not_started, name='mark_not_started'),
    path('tasks/<int:pk>/in_progress/', views.mark_in_progress, name='mark_in_progress'),
]
