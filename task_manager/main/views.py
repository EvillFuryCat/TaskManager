from rest_framework import viewsets
import django_filters


from .serializers import TaskSerializer, UserSerializer, TagSerializer
from .models import Task, User, Tag


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = User
        fields = ("username",)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer
    filterset_class = UserFilter


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskFilter(django_filters.FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(
        field_name="tags__title", queryset=Tag.objects.all()
    )
    author = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    executor = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    status = django_filters.ChoiceFilter(choices=Task.Status.choices)

    class Meta:
        model = Task
        fields = ["tags", "status", "author", "executor"]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().select_related("executor").order_by("id")
    serializer_class = TaskSerializer
    filterset_class = TaskFilter
