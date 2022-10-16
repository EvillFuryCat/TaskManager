from rest_framework import serializers
from .models import tags, user, task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user.User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "phone",
        )


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = tags.Tag
        fields = (
            "id",
            "title",
        )


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = task.Task
        fields = (
            "id"
            "title",
            "description",
            "date_creation",
            "date_change",
            "deadline",
            "author",
            "executor",
            "tags",
            "priority",
            "status",
        )
