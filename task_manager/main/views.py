from rest_framework import generics, viewsets
from django.shortcuts import render

from .serializers import TaskSerializer, UserSerializer, TagSerializer
from .models import Task, User


class TaskAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.prefetch_related("tags")
    serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().select_related("executor").order_by("id")
    serializer_class = TaskSerializer
