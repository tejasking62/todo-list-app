from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET': 
        todos = Task.objects.all()
        serializer = TaskSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, Update, Delete Task
@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Task completed
@api_view(['POST'])
def mark_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = 'completed'
    task.save()
    return Response({'message': 'Task completed!'})

# Task not started
@api_view(['POST'])
def mark_not_started(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = 'not_started'
    task.save()
    return Response({'message': 'Task not started'})

# Task in progress
@api_view(['POST'])
def mark_in_progress(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = 'in_progress'
    task.save()
    return Response({'message': 'Task in progress'})

