from rest_framework import generics
from django.shortcuts import render

from .serializers import TaskSerializer

from .models import Task


class TaskAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer