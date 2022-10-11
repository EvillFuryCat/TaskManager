from rest_framework import generics, viewsets
from django.shortcuts import render
import django_filters


from .serializers import TaskSerializer, UserSerializer, TagSerializer
from .models import Task, User, Tag


class TaskAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = User
        fields = ("name",)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer
    filterset_class = UserFilter


class TagViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.prefetch_related("tags")
    serializer_class = TagSerializer


class TaskFilter(django_filters.FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(
        field_name="tags__title", queryset=Tag.objects.all()
    )
    author = django_filters.CharFilter(lookup_expr="icontains")
    executor = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Task
        fields = ["tags", "author", "executor"]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().select_related("executor").order_by("id")
    serializer_class = TaskSerializer
    filterset_class = TaskFilter
